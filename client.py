import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

def aiProcess(command):
    client = OpenAI(
        api_key=os.getenv("groq_api_key"),
        base_url="https://api.groq.com/openai/v1"
    )

    completion = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[
            {
                "role": "system",
                "content": "You are Jarvis. Give short, helpful answers suitable for a voice assistant."
            },
            {
                "role": "user",
                "content": command
            }
        ]
    )

    return completion.choices[0].message.content