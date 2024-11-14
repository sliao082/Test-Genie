import ollama

# extract 

def test_questions(file):
    test_prompts = []
    test_answers = []
    test_file = file
    with open(test_file, "r") as file:
        content = file.readlines()
        prompts = ""
        answers = ""
        for sentence in content:
            if sentence.startswith("Q") or sentence.startswith("S"):
                if answers != "":
                    test_prompts.append(prompts)
                    prompts = ""
                    test_answers.append(answers)
                    answers = ""
                prompts += (sentence[2:] + "\n")
            elif sentence.startswith("A"):
                answers += (sentence[2:] + "\n")
        if answers and sentence: 
            test_prompts.append(prompts)
            test_answers.append(answers)

    return test_prompts, test_answers

import re

def normalize(text):
    text = re.sub(r'\s+', ' ', text)  
    text = re.sub(r'[^\w\s]', '', text)  
    return text.strip().lower()  

def correctness(ollama_response, answers):
    cnt = 0
    for i in range(len(answers)):
        normalized_response = normalize(ollama_response[i])
        normalized_answer = normalize(answers[i])
        print(f"Ollama: {normalized_response}")
        print(f"Answer: {normalized_answer}")
        print("*"*50)
        if normalized_answer == normalized_response:
            cnt += 1
    
    return f"{(cnt / len(answers)) * 100}%"

# Example usage with your test case
file = "/Users/sanhorn/Desktop/UIUC/Junior/CS222/Test-Genie/Test/test2.txt"
test_prompts, test_answers = test_questions(file)
# breakpoint()

ollama_response = []
for i, prompt in enumerate(test_prompts):
    response = ""
    
    system_message = {
        "role": "system", 
        "content": "This is a multiple choice assignent. Give out the response based on the given selections."
    }

    user_message = {
        "role": "user",
        "content": prompt
    }

    stream = ollama.chat(
        model="llama3.2",
        messages=[system_message, user_message],
        stream=True,
    )
    
    for chunk in stream:
        response += chunk["message"]["content"]
    
    ollama_response.append(response)

value = correctness(ollama_response, test_answers)
print(value)
