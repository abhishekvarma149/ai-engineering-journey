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

from pydantic import BaseModel
class Ticket(BaseModel):
    name: str
    email: str
    issue:str
    phone_number: str

schema = Ticket.model_json_schema()

response_format = {
    "type":"json_object"
}

system_prompt = f"""
Extract the personal inofrmatio from the ticket stricty based on this schema: {schema} and give me in json output"""

message_system={
    "role":"system",
    "content":system_prompt
}


text = "Hello my name is Abhishek. I have an iphone which is not working properly. My address is Kerala. My email is vvhh2661@gmail.com. My phone number is 9235823492."

prompt = f"""
This is customer ticket please exact the personal information from this {text}"""

message = {
    "role":role,
    "content":prompt
}
messages = [message_system,message]

response = client.chat.completions.create(model=model, messages=messages, response_format=response_format)


print("################################")

answer = response.choices[0].message.content
print(answer)

#how do we ready 
import json
raw_JSON = answer
data_file = json.loads(raw_JSON)
ticket = Ticket(**data_file)

print(ticket.name)
print(ticket.email)
print(ticket.issue)
print(ticket.phone_number)