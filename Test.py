import os
from google import genai

gemini_api_key = os.environ["GEMINI_API_KEY"]

client = genai.Client(api_key=gemini_api_key)

post_text = """
AI agents are becoming much more useful as they gain access to real tools,
memory, and better reasoning.
"""

prompt = f"""
You are an AI and technology content assistant for X.

Analyze this X post:

{post_text}

Create ONE thoughtful reply to this post.

Rules:
- Maximum 280 characters.
- Add genuine value.
- Directly relate to the original post.
- Sound natural and human.
- Do not praise unnecessarily.
- Do not ask people to follow me.
- Do not promote my account.
- Do not use hashtags.
- Do not use excessive emojis.
- Do not copy the original post.
- Do not make unsupported claims.
- No politics.
- No harassment.
- No spam.
- Return ONLY the reply.
"""

response = client.models.generate_content(
    model="gemini-3-flash",
    contents=prompt
)

reply = response.text.strip()

if len(reply) > 280:
    reply = reply[:277].rstrip() + "..."

print("Suggested reply:")
print(reply)
