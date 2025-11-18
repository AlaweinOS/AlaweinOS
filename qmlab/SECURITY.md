# Security Guidelines

## Reporting
- For vulnerabilities, open a private issue or email the maintainers.

## CSP
- Configured in `vercel.json`.
- `script-src` excludes `'unsafe-eval'`; inline allowed for now.
- Reports: `report-uri /csp-report` (aggregated, no backend processing).

## Runtime Flags
- `VITE_SECURITY_DEEP_HOOKS`: when `true`, enables `eval` hook in `SecurityMonitor`.
- `VITE_SECURITY_CONSOLE_MONITOR`: when `true`, wraps `console` methods to flag suspicious access.
- Production defaults: both disabled; incident POST is a no-op in prod.

## Analytics
- GTM/GA4 via `src/lib/analytics.ts`. If `window.dataLayer` is missing, events are no-ops.

## Input/Output
- Use `InputValidator` from `src/lib/security.ts` for sanitization/validation.


