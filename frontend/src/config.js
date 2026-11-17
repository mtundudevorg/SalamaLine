// Single place for runtime configuration. Values come from .env (see .env.example).
// Mock (offline) mode: used automatically while VITE_API_BASE_URL is NOT set, so the whole interface
// works before the backend exists. Set VITE_API_BASE_URL (or VITE_USE_MOCK=false) to talk to the real backend.
const RAW_BASE = import.meta.env.VITE_API_BASE_URL
export const USE_MOCK = import.meta.env.VITE_USE_MOCK ? import.meta.env.VITE_USE_MOCK === 'true' : !RAW_BASE
export const API_BASE_URL = (RAW_BASE || '/api/v1').replace(/\/+$/, '')
export const REQUEST_TIMEOUT_MS = Number(import.meta.env.VITE_REQUEST_TIMEOUT_MS) || 15000
