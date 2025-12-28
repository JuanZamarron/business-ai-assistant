from openai import OpenAI
from app.config import settings
import openai

c = OpenAI(api_key=settings.OPENAI_API_KEY)

print("openai version:", openai.__version__)
print("Has responses:", hasattr(c, "responses"))
