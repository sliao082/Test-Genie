from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from api.uplaod import router as upload_router
from services.ollama_service import get_response_from_ollama

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(upload_router, prefix="/api/upload", tags=["upload"])

class MessageRequest(BaseModel):
    system_message: str
    user_message: str
    model: str = "llama3.2"

@app.post("/api/generate-response")
async def generate_response(request: MessageRequest):
    try:
        response = get_response_from_ollama(
            system_message_content=request.system_message,
            user_message_content=request.user_message,
            model=request.model
        )
        return {"response": response}

    except Exception as e:
        print(f"Error generating response: {e}")
        raise HTTPException(status_code=500, detail="Failed to generate response from Ollama model.")