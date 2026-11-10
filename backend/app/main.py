from fastapi import FastAPI
from fastapi.responses import JSONResponse

from app.api.routes.health import router as health_router
from app.core.config import settings

app = FastAPI(
    title="Cyber Consequence Engine API",
    version="0.1.0",
    description="CCE backend foundation API.",
)

app.include_router(health_router, prefix="/api")


@app.exception_handler(Exception)
async def unexpected_error_handler(_request, exc: Exception) -> JSONResponse:
    # Do not expose exception details or stack traces to API clients.
    settings.logger.exception("Unhandled application error: %s", type(exc).__name__)
    return JSONResponse(
        status_code=500,
        content={"error": {"code": "internal_error", "message": "Internal server error"}},
    )
