
const API_BASE_URL = (
  import.meta.env.VITE_API_BASE_URL || '/api/v1'
).replace(/\/+$/, '')

async function request(path, options = {}) {
  let response

  try {
    response = await fetch(`${API_BASE_URL}${path}`, {
      ...options,
      headers: {
        Accept: 'application/json',
        ...(options.body
          ? { 'Content-Type': 'application/json' }
          : {}),
        ...options.headers,
      },
      credentials: 'include',
    })
  } catch {
    throw new Error(
      'Imeshindikana kuwasiliana na server. Hakikisha backend inafanya kazi.'
    )
  }

  if (!response.ok) {
    const message = await response.text().catch(() => '')

    throw new Error(
      message || `Ombi limeshindwa. HTTP ${response.status}`
    )
  }

  if (response.status === 204) return null

  const contentType = response.headers.get('content-type') || ''

  if (!contentType.includes('application/json')) {
    throw new Error('Server imerudisha majibu yasiyo JSON.')
  }

  return response.json()
}

function buildQuery(params = {}) {
  const query = new URLSearchParams()

  Object.entries(params).forEach(([key, value]) => {
    if (value !== undefined && value !== null && value !== '') {
      query.set(key, String(value))
    }
  })

  const result = query.toString()
  return result ? `?${result}` : ''
}

export const api = {
  getRegions: () => request('/regions'),

  getDistricts: (regionId) =>
    request(`/regions/${encodeURIComponent(regionId)}/districts`),

  searchVerifiedServices: (params = {}) =>
    request(`/services${buildQuery(params)}`),

  createSupportRequest: (payload) =>
    request('/support-requests', {
      method: 'POST',
      body: JSON.stringify(payload),
    }),

  getResponderProfile: () =>
    request('/responder/me'),

  getAssignedCases: (params = {}) =>
    request(`/responder/cases${buildQuery(params)}`),

  updateCaseStatus: (caseId, status) =>
    request(`/responder/cases/${encodeURIComponent(caseId)}/status`, {
      method: 'PATCH',
      body: JSON.stringify({ status }),
    }),

  getPartnerAnalytics: () =>
    request('/partner/analytics'),
}
