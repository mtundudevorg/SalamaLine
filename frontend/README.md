# SalamaLine — Frontend

A responsive, bilingual (Kiswahili / English) React + Vite + Tailwind CSS frontend for SalamaLine, a confidential safety-information and human-support pathway for girls and young people in Tanzania.

## Features
- Responsive layout for desktop, tablet and mobile.
- Custom SalamaLine brand mark and neumorphic visual design.
- Kiswahili / English interface toggle.
- Light and dark theme controls.
- Quick Exit navigation with an honest limitation notice.
- Safe-information library covering education access, child/forced marriage, FGM, violence, wellbeing and digital safety.
- Region and district selector covering Tanzania's regions with a verified-provider-only directory state.
- Consent-aware support request form with optional contact details and contact preference.
- Guided support flow that routes users toward region-based next steps using predefined choices.
- Responder workspace: sign-in, assigned-case list, status filter, accept/close actions and refresh, all via the API.
- Basic-phone USSD/SMS integration notes in the guided-support area.
- Accessibility considerations: semantic controls, keyboard focus states, responsive layouts and reduced-motion preference.

## Technology stack
- React 18
- Vite 6
- JavaScript (ES modules)
- Tailwind CSS 3 (configured; detailed component styling is in `src/index.css`)
- Lucide React icons

## Run locally
1. Install Node.js 20+.
2. Extract this project and open the folder in VS Code.
3. Open the VS Code terminal in this folder.
4. Run:

```bash
npm install
npm run dev
```

5. Open the local URL printed by Vite.
6. Verify production compilation with:

```bash
npm run build
npm run preview
```

## Backend integration
The frontend is complete and calls the backend through a single layer, `src/services/api.js`. Endpoints, request/response shapes and the integration steps are in **[API_CONTRACT.md](./API_CONTRACT.md)**. Configure with `.env` (see `.env.example`). If the backend is unreachable the interface shows clear error states and never pretends a request was sent.

## Production safety requirements
- Do not store sensitive request data in browser local storage.
- Enforce responder authentication, role-based permissions, region/case assignment and audit logging on the server.
- Do not reveal another responder's cases or any user's private information to other users.
- Use professional-reviewed, versioned content for health, legal and safeguarding topics. Do not use open-ended AI to invent medical/legal advice.
- Verify every service listing and contact detail with a named local partner before displaying it as available.
- Implement consent-first human follow-up, safe-contact preferences, escalation procedures and contact-data deletion after case closure.
- Obtain telecom/operator integration for USSD short codes, SMS, IVR voice calls and WhatsApp. Short codes shown in the UI are placeholders, not live numbers.
- Quick Exit only navigates away; it cannot guarantee browser history, notifications or records are erased.
- Complete a privacy impact assessment, safeguarding review, accessibility testing and security testing before pilot/production.

## Important scope note
Frontend code alone cannot safely deliver a live safeguarding service. Authentication, case routing, provider verification, consent handling, data deletion and telecom (USSD/SMS) integration must be provided and secured by the backend and partners. The guide uses predefined choices, not a connected AI model. The USSD short code shown in the guide is a placeholder.
