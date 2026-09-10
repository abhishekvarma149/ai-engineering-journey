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

prompt1 = "Hi"
prompt2 = "Explain time travel in detail in 100 words"
prompt3 = "Write a 1000 word essay on the history of artificial intelligence"

prompts = [prompt1, prompt2, prompt3]
for prompt in prompts:
    message={
    "role": role,
    "content": prompt
    }
    messages = [message]
    response = client.chat.completions.create(model=model, messages=messages, temperature = 1,max_tokens=50)
    usage = response.usage
    print(f"Prompt: {prompt} --> your_tokens: {usage.prompt_tokens} completion_tokens: {usage.completion_tokens}  total_tokens: {usage.total_tokens} Finish Reason: {response.choices[0].finish_reason}")


# print("################################")

# answer = response.choices[0].message.content
# print(answer)