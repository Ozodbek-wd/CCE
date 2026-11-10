# CCE Foundation Architecture

- `android/`: Kotlin/Jetpack Compose client. Separate UI and data/domain packages.
- `backend/`: FastAPI service, API routers, configuration, tests.
- Android communicates with backend over HTTP/JSON (not wired in this foundation).
- Provider/LLM secrets are backend-only; never ship them in the APK.
- Future security simulations must use isolated virtual models and have no write path to real systems.
