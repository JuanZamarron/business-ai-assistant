# Business Assistant API (FastAPI + OpenAI)

Backend en Python que expone un endpoint `/chat` para consultas de negocio usando OpenAI.

## Stack
- FastAPI
- OpenAI Python SDK (Responses API)
- Pydantic

## Setup
1) `pip install -r requirements.txt`
2) Copia `.env.example` a `.env` y agrega `OPENAI_API_KEY`
3) `uvicorn app.main:app --reload --port 8000`

## Endpoints
- GET `/health`
- POST `/chat`
