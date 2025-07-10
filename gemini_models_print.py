import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv(".env")

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=GEMINI_API_KEY)

models = genai.list_models()

for model in models:
    if "flash" in model.name:
        print(model.name)
