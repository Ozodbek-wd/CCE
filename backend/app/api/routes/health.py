from datetime import datetime, timezone
from fastapi import APIRouter

router = APIRouter(tags=["health"])


@router.get("/health", summary="Check API health")
def health_check() -> dict[str, str]:
    return {
        "status": "healthy",
        "service": "CCE Backend",
        "version": "0.1.0",
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }
