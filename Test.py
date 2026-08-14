import os
from google import genai

api_key = os.environ["GEMINI_API_KEY"]

client = genai.Client(api_key=api_key)

prompt = """
You are an AI and technology content creator for X.

Generate ONE original X post about AI or technology.

Rules:
- Maximum 280 characters.
- Write in simple, natural English.
- Make it useful or interesting.
- Target a worldwide audience.
- No politics.
- No religion.
- No controversial topics.
- No hate, harassment or accusations.
- No illegal activity.
- No hacking, malware or cybercrime instructions.
- No medical or financial advice.
- No fake statistics.
- Do not invent news.
- Do not copy another person's post.
- Do not use hashtags.
- Do not use emojis excessively.
- Do not add an introduction or explanation.
- Return ONLY the final X post.
"""

response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents=prompt
)

print(response.text.strip())
