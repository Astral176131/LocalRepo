import openai
import os
import pandas as pa
import time

openai.api_key= ""
messages={"role": "system", "content":"You are an AI asistant"}
while True:
    message=input("User: ")
    if message:
        chat=openai.chat.completions.create(model="gpt-4",
        messages=[{"role": "system", "content":"You are an AI asistant"},{"role":"user","content":message}]
        ,temperature=0.5)
        reply=chat.choices[0].message['content'].strip()
        print(f"ChatBot: {reply}")
        messages.append({"role":"assistant","content":reply})
