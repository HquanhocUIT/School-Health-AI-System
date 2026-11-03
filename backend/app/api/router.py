"""Top-level API router."""

from fastapi import APIRouter

api_router = APIRouter()


@api_router.get("/", tags=["system"], summary="API welcome")
def root() -> dict[str, str]:
    return {"message": "Welcome to SchoolHealth API"}


@api_router.get("/health", tags=["system"], summary="Health check")
def health_check() -> dict[str, str]:
    return {"status": "healthy", "message": "SchoolHealth backend is running"}
