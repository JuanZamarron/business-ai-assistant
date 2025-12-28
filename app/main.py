from fastapi import FastAPI, HTTPException
from .schemas import ChatRequest, ChatResponse
from .config import settings
from .openai_client import generate_answer

app = FastAPI(title="Business Assistant API", version="0.1.0")

@app.get("/health")
def health():
    return {"status": "ok", "env": settings.APP_ENV}

@app.post("/chat", response_model=ChatResponse)
def chat(payload: ChatRequest):
    try:
        answer = generate_answer(payload.message, settings.OPENAI_MODEL)
        return ChatResponse(answer=answer, model=settings.OPENAI_MODEL)
    except Exception as e:
        # En producción: loggear bien y mapear errores específicos
        raise HTTPException(status_code=500, detail=f"AI error: {str(e)}")
