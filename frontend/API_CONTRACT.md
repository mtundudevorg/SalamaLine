# SalamaLine — API contract (frontend expectations)

All HTTP lives in **`src/services/api.js`**. If the backend uses different paths or field names,
change them there only (paths in `api`, field names in the `normalize*` helpers). No other file needs to change.

- Base URL: `VITE_API_BASE_URL` (default `/api/v1`). Requests are JSON and sent with `credentials: 'include'`
  (session via **httpOnly cookie** set by the backend; the frontend never stores tokens).
- Cross-domain deployment: backend must send `Access-Control-Allow-Origin: <frontend origin>` and
  `Access-Control-Allow-Credentials: true`. In local dev set `VITE_DEV_PROXY_TARGET` to avoid CORS.
- Errors: any non-2xx. Optional body `{ "message": "...", "code": "...", "errors": {...} }`.
  The UI shows its own translated messages: 401/403 → invalid credentials/no access, 400/422 → invalid data, 429 → too many attempts, anything else/unreachable → generic.
- A 2xx response that is not JSON is treated as a failure (except 204).

| Purpose | Request | Response |
|---|---|---|
| Regions & districts | `GET /regions` | `[{ "name": "Mbeya", "districts": ["Mbeya City", ...] }]` or `{ "Mbeya": ["Mbeya City"] }`. If this call fails the app falls back to its built-in list. |
| Verified services | `GET /services?region=&district=&q=` | `[{ id, name, category, region, district, address, phone, hours, verified }]` (or `{ "items": [...] }`). **Verified providers only.** Empty list shows the "no verified service" state. |
| Submit support request | `POST /support-requests` | `201 { "reference": "SL-889900" }` (`id` also accepted) |
| Responder sign in | `POST /responder/auth/login` body `{ email, password }` | `200` + session cookie; `401` on bad credentials |
| Responder sign out | `POST /responder/auth/logout` | `204` |
| Current responder | `GET /responder/me` | `{ name, email }`; `401` when not signed in (used to restore a session) |
| Assigned cases | `GET /responder/cases` | `[{ id, topic, region, district, status, createdAt }]` — **only cases assigned to this responder** |
| Update case status | `PATCH /responder/cases/:id/status` body `{ "status": "active" \| "closed" }` | updated case (or `204`) |

## Support request body (`POST /support-requests`)
```json
{
  "topic": "education | marriage | fgm | violence | mental | digital",
  "region": "Mbeya",
  "district": "Mbeya City",
  "details": "optional free text or null",
  "anonymous": false,
  "contactMethod": "sms | whatsapp | call | null",
  "contact": "optional phone/contact or null",
  "consent": true,
  "language": "sw | en"
}
```
- `anonymous: true` ⇒ `contactMethod`, `contact` are `null` and `consent` is `false`.
- Backend should reject `anonymous: false` without `consent: true` and minimise/encrypt stored data.

## Status values
UI uses `new | active | closed`. Backend synonyms accepted when reading: `open/pending → new`, `in_progress/assigned → active`, `resolved → closed`.
To send different values, edit `STATUS_TO_API` in `src/services/api.js`.

## Test mode vs real backend
While `VITE_API_BASE_URL` is **not set**, the app runs in offline test mode (`src/services/mockApi.js`): every page and form works, nothing is sent anywhere, and the success screen says so. Setting `VITE_API_BASE_URL` (or `VITE_USE_MOCK=false`) switches to the real backend.

## Switching on at integration time
1. `cp .env.example .env` and uncomment/set `VITE_API_BASE_URL` (and `VITE_DEV_PROXY_TARGET` for local dev).
2. `npm run dev`, then open each page once. Without a reachable backend the app shows clear error states; it never fakes a success.
3. Adjust paths / field names in `src/services/api.js` if the backend differs.
