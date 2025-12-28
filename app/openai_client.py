from openai import OpenAI
from .config import settings

# El SDK oficial lee OPENAI_API_KEY del entorno, pero también puedes pasarlo explícito.
client = OpenAI(api_key=settings.OPENAI_API_KEY)

def generate_answer(user_message: str, model: str) -> str:
    """
    Llamada mínima usando Responses API.
    """
    resp = client.responses.create(
        model=model,
        input=[
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

    # En los ejemplos oficiales se usa output_text como forma simple de obtener el texto final.
    return resp.output_text
