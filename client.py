def aiProcess(command):
    client = OpenAI(
        api_key="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",
        base_url="https://api.groq.com/openai/v1"
    )

    completion = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[
            {
                "role": "system",
                "content": "You are a virtual assistant named Jarvis. Give short, helpful answers suitable for a voice assistant."
            },
            {
                "role": "user",
                "content": command
            }
        ]
    )

    return completion.choices[0].message.content