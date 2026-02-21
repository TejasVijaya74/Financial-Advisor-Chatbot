import google.generativeai as genai
from app.core.config import Settings
from app.core.logger import setup_logger

logger = setup_logger()

genai.configure(api_key=Settings.GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-1.5-flash")


def generate_response(prompt: str) -> str:
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        logger.error(f"Gemini API error: {e}")
        return "Sorry, something went wrong."