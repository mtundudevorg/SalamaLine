import { API_BASE_URL, REQUEST_TIMEOUT_MS, USE_MOCK } from '../config.js'
import { mockApi } from './mockApi.js'

/**
 * SalamaLine API client — the ONLY file that knows about HTTP and backend field names.
 * To adapt to the real backend, change paths / field names here (see API_CONTRACT.md).
 * UI components work with the normalised shapes returned by the normalize* helpers.
 */

export class ApiError extends Error {
  constructor(message, { status = 0, code = 'UNKNOWN', errors } = {}) {
    super(message)
    this.name = 'ApiError'
    this.status = status   // HTTP status, or 0 when the server could not be reached
    this.code = code       // NETWORK | TIMEOUT | INVALID_RESPONSE | backend-provided code
    this.errors = errors   // optional field-level validation errors from the backend
  }
}

const toQuery = (params = {}) => {
  const q = new URLSearchParams(Object.entries(params).filter(([, v]) => v != null && v !== ''))
  const s = q.toString()
  return s ? `?${s}` : ''
}

async function request(path, { method = 'GET', body, params, signal } = {}) {
  const controller = new AbortController()
  const timer = setTimeout(() => controller.abort('timeout'), REQUEST_TIMEOUT_MS)
  if (signal) signal.addEventListener('abort', () => controller.abort('aborted'), { once: true })
  let response
  try {
    response = await fetch(`${API_BASE_URL}${path}${toQuery(params)}`, {
      method,
      credentials: 'include', // session cookie (httpOnly) set by the backend
      headers: { Accept: 'application/json', ...(body !== undefined ? { 'Content-Type': 'application/json' } : {}) },
      body: body !== undefined ? JSON.stringify(body) : undefined,
      signal: controller.signal,
    })
  } catch (err) {
    const timedOut = controller.signal.reason === 'timeout'
    throw new ApiError(timedOut ? 'Request timed out' : 'Network error', { status: 0, code: timedOut ? 'TIMEOUT' : 'NETWORK' })
  } finally {
    clearTimeout(timer)
  }

  const isJson = (response.headers.get('content-type') || '').includes('json')
  const data = response.status === 204 ? null : isJson ? await response.json().catch(() => null) : null

  if (!response.ok) {
    throw new ApiError(typeof data?.message === 'string' ? data.message.slice(0, 200) : `HTTP ${response.status}`, {
      status: response.status, code: data?.code || 'HTTP_ERROR', errors: data?.errors,
    })
  }
  // A 2xx that is not JSON (e.g. the dev server returning index.html because no backend is running)
  // must never be treated as success.
  if (response.status !== 204 && !isJson) throw new ApiError('Unexpected response from server', { status: response.status, code: 'INVALID_RESPONSE' })
  return data
}

/* ---------- Normalisers: backend shape -> UI shape (edit here if field names differ) ---------- */

const list = (data) => (Array.isArray(data) ? data : Array.isArray(data?.items) ? data.items : Array.isArray(data?.data) ? data.data : [])

// UI statuses: new | active | closed
const STATUS_FROM_API = { new: 'new', open: 'new', pending: 'new', active: 'active', in_progress: 'active', assigned: 'active', closed: 'closed', resolved: 'closed' }
const STATUS_TO_API = { active: 'active', closed: 'closed' }
export const normalizeStatus = (s) => STATUS_FROM_API[String(s || '').toLowerCase()] || 'new'

/** Accepts { "Mbeya": ["Mbeya City", ...] } or [{ name, districts: [string | {name}] }]. Returns { region: [districts] } or null. */
export function normalizeRegions(data) {
  const out = {}
  const arr = list(data)
  if (arr.length) {
    arr.forEach((r) => { if (r?.name) out[r.name] = (r.districts || []).map((d) => (typeof d === 'string' ? d : d?.name)).filter(Boolean) })
  } else if (data && typeof data === 'object') {
    Object.entries(data).forEach(([k, v]) => { if (Array.isArray(v)) out[k] = v.map((d) => (typeof d === 'string' ? d : d?.name)).filter(Boolean) })
  }
  return Object.keys(out).length ? out : null
}

export const normalizeService = (s) => ({
  id: s.id ?? `${s.name}-${s.district || ''}`,
  name: s.name || '',
  category: s.category || '',
  region: s.region || '',
  district: s.district || '',
  address: s.address || '',
  phone: s.phone || s.contact || '',
  hours: s.hours || s.openingHours || '',
  verified: s.verified !== false,
})

export const normalizeCase = (c) => ({
  id: String(c.id ?? c.reference ?? ''),
  topic: c.topic || '',
  region: c.region || '',
  district: c.district || '',
  status: normalizeStatus(c.status),
  created: c.createdAt || c.created_at || c.created || '',
})

const formatDate = (v) => { const d = new Date(v); return v && !Number.isNaN(d.getTime()) ? d.toLocaleString() : v || '' }

/* ---------- Endpoints ---------- */

const realApi = {
  // Reference data
  getRegions: async () => normalizeRegions(await request('/regions')),

  // Public directory (backend must return verified providers only)
  searchVerifiedServices: async ({ region, district, q } = {}) =>
    list(await request('/services', { params: { region, district, q } })).map(normalizeService),

  // Support request — returns { reference }
  createSupportRequest: async (payload) => {
    const res = await request('/support-requests', { method: 'POST', body: payload })
    return { reference: String(res?.reference ?? res?.id ?? '') }
  },

  // Responder session
  login: (email, password) => request('/responder/auth/login', { method: 'POST', body: { email, password } }),
  logout: () => request('/responder/auth/logout', { method: 'POST' }),
  getResponderProfile: async () => { const p = await request('/responder/me'); return { name: p?.name || '', email: p?.email || '' } },

  // Responder cases (server must only return cases assigned to the signed-in responder)
  getAssignedCases: async (params = {}) =>
    list(await request('/responder/cases', { params })).map((c) => ({ ...normalizeCase(c), created: formatDate(normalizeCase(c).created) })),
  updateCaseStatus: async (caseId, status) => {
    const c = await request(`/responder/cases/${encodeURIComponent(caseId)}/status`, { method: 'PATCH', body: { status: STATUS_TO_API[status] || status } })
    return c ? normalizeCase(c) : { id: String(caseId), status }
  },

  // Partner analytics (aggregate only)
  getPartnerAnalytics: () => request('/partner/analytics'),
}

// Real backend when configured; otherwise the in-memory mock so the UI is fully usable before integration.
export const api = USE_MOCK ? mockApi : realApi
