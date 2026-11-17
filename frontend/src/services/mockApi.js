// In-memory stand-in for the backend. Used ONLY while VITE_API_BASE_URL is not set (see src/config.js).
// Nothing is stored or sent anywhere; data disappears when the page reloads.
const wait = (ms = 450) => new Promise((r) => setTimeout(r, ms))
const unauthorized = () => Object.assign(new Error('Unauthorized'), { status: 401, code: 'UNAUTHORIZED' })
let cases = []
let signedIn = false

export const mockApi = {
  getRegions: async () => null, // UI falls back to its built-in region list
  searchVerifiedServices: async () => { await wait(); return [] },
  createSupportRequest: async (p) => {
    await wait()
    const reference = `SL-${Date.now().toString().slice(-6)}`
    cases = [{ id: reference, topic: p.topic, region: p.region, district: p.district || '', status: 'new', created: new Date().toLocaleString() }, ...cases]
    return { reference }
  },
  login: async () => { await wait(); signedIn = true },
  logout: async () => { signedIn = false },
  getResponderProfile: async () => { if (!signedIn) throw unauthorized(); return { name: '', email: '' } },
  getAssignedCases: async () => { await wait(200); if (!signedIn) throw unauthorized(); return cases.map((c) => ({ ...c })) },
  updateCaseStatus: async (id, status) => { await wait(200); cases = cases.map((c) => (c.id === id ? { ...c, status } : c)); return { id, status } },
  getPartnerAnalytics: async () => ({}),
}
