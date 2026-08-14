
import os
from google import genai

api_key = os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

prompt = """
You are my personal X content creator.

Generate ONE interesting and useful tweet for my X account.

Topics can include:
AI, technology, science, interesting facts, education, productivity and current trends.

Rules:
- Keep it concise.
- Make it interesting.
- Use simple English.
- Do not use hashtags.
- Do not invent facts.
- Do not add explanations before or after the tweet.
- Return only the tweet.
"""

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=prompt
)

print(response.text)
