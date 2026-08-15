import os
import requests
from google import genai

gemini_api_key = os.environ["GEMINI_API_KEY"]
x_access_token = os.environ["X_ACCESS_TOKEN"]

client = genai.Client(api_key=gemini_api_key)

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

tweet = response.text.strip()

if len(tweet) > 280:
    tweet = tweet[:277].rstrip() + "..."

print("Generated tweet:")
print(tweet)

headers = {
    "Authorization": f"Bearer {x_access_token}",
    "Content-Type": "application/json"
}

data = {
    "text": tweet
}

result = requests.post(
    "https://api.x.com/2/tweets",
    headers=headers,
    json=data,
    timeout=30
)

print("X API status:", result.status_code)
print("X API response:", result.text)

result.raise_for_status()

print("Tweet posted successfully.")
