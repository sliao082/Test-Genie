from fastapi import APIRouter
from services.ollama_service import generate_quiz_questions

router = APIRouter()

@router.post("/generate-quiz")
async def generate_quiz(content: str):
    quiz_questions = generate_quiz_questions(content)
    return {"quiz_questions": quiz_questions}