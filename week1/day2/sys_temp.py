import os 
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
my_api_key = os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("GROQ_API_KEY is not set in the environment variables.")

client = Groq(api_key=my_api_key)

model = "openai/gpt-oss-20b"

role = "user"

prompt = "Suggest a name for my food company"

message_system={
    "role": "system",
    "content": "You are a brand manager who suggest name for my food company. Name should be in one word, suggest one name only"
}

message = {
    "role":role,
    "content":prompt
}
messages = [message]

# temperature by default is 0 meaning safe, range is [0,2]
response = client.chat.completions.create(model=model, messages=messages, temperature = 1)
# print(response)

print("################################")

answer = response.choices[0].message.content
print(answer)