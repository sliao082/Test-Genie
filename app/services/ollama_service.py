import ollama

def get_response_from_ollama(system_message_content, user_message_content, model="llama3.2"):
    response = ""

    system_message = {
        "role": "system", 
        "content": system_message_content        
    }

    user_message = {
        "role": "user",
        "content": user_message_content
    }

    try:
        stream = ollama.chat(
            model=model,
            messages=[system_message, user_message],
            stream=True
        )

        for chunk in stream:
            response += chunk["message"]["content"]

    except Exception as e:
        print(f"An error occurred while communicating with the Ollama model: {e}")
        response = "There was an error processing the request."

    return response