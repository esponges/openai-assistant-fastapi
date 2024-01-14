from fastapi import APIRouter
from app.model.services.lesson_planner import LessonPlannerService

lesson_planner_router = APIRouter()

@lesson_planner_router.get("/get_prediction")
def get_prediction(q: str):
    "Get prediction from the OpenAI API"
    return LessonPlannerService().get_prediction(q)
