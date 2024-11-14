import ollama

response = ""

system_message = {
    "role": "system", 
    "content": "Give me 3 sentences."        
}

user_message = {
    "role": "user",
    "content": "MIT vs UIUC?"
}

stream = ollama.chat(
    model="llama3.2",
    messages=[system_message, user_message],
    stream=True,
)

for chunk in stream:
    response += chunk["message"]["content"]
    
print(response)