from fastapi import APIRouter
from app.core.config import settings

api_router = APIRouter(prefix=settings.api_prefix)

@api_router.get(
    "/health",
    summary="健康检查",
    description="检查后端服务是否正常运行。"
)
async def health_check()->dict[str, str]:
    """
    返回服务健康状态。
    Returns:
        dict[str, str]:固定返回"status=OK"的状态对象。
        """
    return {"status": "ok"}