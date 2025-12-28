from openai import OpenAI
from .config import settings

client = OpenAI(api_key=settings.OPENAI_API_KEY)

def generate_answer(user_message: str, model: str) -> str:
    resp = client.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "system",
                "content": (
                    "Eres un asistente para negocio. Responde claro, profesional y con bullets cuando ayude. "
                    "Si falta información, pregunta lo mínimo necesario."
                ),
            },
            {"role": "user", "content": user_message},
        ],
    )
    return resp.choices[0].message.content
