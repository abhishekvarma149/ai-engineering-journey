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

def llm_ans(prompt):
    message={
        "role": "user",
        "content": prompt
    }
    messages = [message]
    response = client.chat.completions.create(model=model,messages=messages)
    ans=response.choices[0].message.content
    return ans

bad_prompt="""
This is a user complaint:
My laptop is not working
Classify this"""

role_prompt="""
#ROLE
You are a support assistant at a mobile/laptop company
#TASK
You have to classify the issue in a category
#CONSTRAINT
You have to classify the issue in one of categories namely billing,technical,return
#OUTPUT FORMAT
Your answer should be in one word only. The one word should be one of categories given in constraints
#EXAMPLE
For instant if a user complain says that he wants a refund then the category is Return
#FALLBACK
If the issue is unrealted to any of the categories mentioned  in constraints, then the answer should be other
This is user complaint:
My laptop is not working

"""

print(llm_ans(role_prompt))