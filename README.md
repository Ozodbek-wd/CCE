# CYBER CONSEQUENCE ENGINE (CCE)

Foundation project: Android (Kotlin + Jetpack Compose) and Python (FastAPI), kept separate.

## Backend (Python 3.10+)
```bash
cd backend
python -m venv .venv
# Linux/macOS:
source .venv/bin/activate
# Windows PowerShell:
# .venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
uvicorn app.main:app --reload
```
Health: http://127.0.0.1:8000/api/health  
API docs: http://127.0.0.1:8000/docs

Test (in another terminal, with backend venv activated):
```bash
cd backend
pytest
```

## Android
Open `android/` in Android Studio (recent stable version), allow Gradle sync, then Run on an emulator/device.
The app currently displays a foundation screen; API integration is intentionally not implemented yet.

## Safety baseline
- Never put LLM/provider API keys in Android resources, source, or build config.
- Keep secrets on backend in environment variables or a secret manager.
- Future simulations must operate only on isolated virtual models and must not alter real systems.
- This foundation does not implement simulations or advanced features.
