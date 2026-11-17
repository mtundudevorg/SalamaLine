import { defineConfig, loadEnv } from 'vite'
import react from '@vitejs/plugin-react'

// If VITE_DEV_PROXY_TARGET is set (e.g. http://localhost:8000), /api requests are proxied
// to the backend during `npm run dev`, so no CORS setup is needed locally.
export default defineConfig(({ mode }) => {
  const env = loadEnv(mode, process.cwd(), '')
  const target = env.VITE_DEV_PROXY_TARGET
  return {
    plugins: [react()],
    server: target ? { proxy: { '/api': { target, changeOrigin: true } } } : {},
  }
})
