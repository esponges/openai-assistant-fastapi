from fastapi import APIRouter

# from api.user.v1.user import user_router as user_v1_router
# from api.auth.auth import auth_router
from api.item.item import item_router
from api.home.home import home_router
from api.model.lesson_planner import lesson_planner_router

router = APIRouter()
router.include_router(item_router, prefix="/item", tags=["item"])
router.include_router(home_router, prefix="", tags=["home"])
router.include_router(lesson_planner_router, prefix="/model", tags=["model"])

__all__ = ["router"]
