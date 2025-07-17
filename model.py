# model.py
from openai import OpenAI

# Replace this with your actual Groq API key
GROQ_API_KEY = "paste your api here"

# Create and return OpenAI-compatible Groq client
client = OpenAI(
    api_key=GROQ_API_KEY,
    base_url="https://api.groq.com/openai/v1"
)

def get_groq_reply(messages, model="llama3-8b-8192"):
    try:
        response = client.chat.completions.create(
            model=model,
            messages=messages,
            stream=True  # << enable streaming
        )
        for chunk in response:
            if chunk.choices[0].delta.content:
                yield chunk.choices[0].delta.content
    except Exception as e:
        yield f"❌ Error: {str(e)}"
