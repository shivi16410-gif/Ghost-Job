# Vercel-only deployment

GhostJob deploys as one Vercel project:

- Vite frontend: static output in `dist/`
- FastAPI backend: Python ASGI function at `api/index.py`
- API calls: same-origin `/api/...` in production

Vercel imports this repository and uses `vercel.json` automatically. Set these environment variables for **Production, Preview, and Development** as appropriate:

```text
ENVIRONMENT=production
REQUIRE_EXTERNAL_PROVIDERS=true
ALLOWED_ORIGINS=https://YOUR_PROJECT.vercel.app

SUPABASE_URL=...
SUPABASE_SERVICE_ROLE_KEY=...
SUPABASE_JWKS_URL=...

TINYFISH_API_KEY=...
TINYFISH_FETCH_URL=https://api.fetch.tinyfish.ai
GEMINI_API_KEY=...
GEMINI_MODEL=gemini-3.8-flash

RESEND_API_KEY=...
FROM_EMAIL=no-reply@YOUR_DOMAIN

VITE_SUPABASE_URL=...
VITE_SUPABASE_PUBLISHABLE_KEY=...
```

Do not set `VITE_API_URL` in Vercel. The frontend automatically uses the same-origin `/api` path.

Before the first production deploy:

1. Apply `supabase/migrations/0001_ghostjob_core.sql`.
2. Configure Supabase Auth redirect URLs for the Vercel domain.
3. Add all variables above in Vercel Project Settings → Environment Variables.
4. Deploy from the repository default branch.
5. Verify `/api/health` and `/api/health/providers` on the deployed domain.

Production requires Supabase because Vercel functions are stateless; the in-memory store is development-only.
