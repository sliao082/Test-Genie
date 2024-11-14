import ollama

# extract 

def test_sparse(file):
    test_question = []
    test_selection = []
    test_answer = []
    
    with open(file, "r") as f:
        content = f.readlines()
        question = ""
        selections = []
        answer = ""
        
        for sentence in content:
            if sentence.startswith("Q:"):
                if question and selections:
                    test_question.append(question.strip())
                    test_selection.append(selections)
                    test_answer.append(answer.strip())
                question = sentence[2:].strip()  
                selections = []  
                answer = ""  
            elif sentence.startswith("S:"):
                selections.append(sentence[2:].strip())  
            elif sentence.startswith("A:"):
                answer = sentence[2:].strip()  
        
        if question and selections:
            test_question.append(question.strip())
            test_selection.append(selections)
            test_answer.append(answer.strip())
    
    return test_question, test_selection, test_answer



file = "/Users/sanhorn/Desktop/UIUC/Junior/CS222/Test-Genie/Test/test3.txt"
test_questions, test_selections, test_answers = test_sparse(file)

''' Idea'''
#### What We can work on? ####
# Question Relevance? 
# Question Hardness (Easy, Medium, Hard)?
# Question Variety?

# Approach 1: Ask to generate questions without answers
### questions without multiple choice selections
### questions with multiple choice selections

# Approach 2: Ask to generate questions with answers
''' '''

test_prompts = []
# for i in range(len(test_questions)):
#     test_prompts.append([test_questions[i], test_answers[i]])
# breakpoint()

conversation_history = [
    {
        "role": "system", 
        "content": "you are a helpful assistant forming new questions. Please keep the question short and concise. Don't give out selections, just output the question. The input question is only a sample question that you can learn from."
    }
]


ollama_response = []
for i, prompt in enumerate(test_questions):
    user_message = {
        "role": "user",
        "content": prompt
    }

    conversation_history.append(user_message)

    response = ""

    stream = ollama.chat(
        model="llama3.2",
        messages=conversation_history,
        stream=True
    )
    
    for chunk in stream:
        response += chunk["message"]["content"]
    
    assistant_message = {
        "role": "assistant", 
        "content": response
    }

    conversation_history.append(assistant_message)
    ollama_response.append(response)

    feedback_message = {
        "role": "user", 
        "content": "You can try to combine topics from sample questions. Don't simply rephrase the sample questions, learn from how the sample questions are asked and ask similar topics or questions with similar topics."
    }
    conversation_history.append(feedback_message)

    print("Sample Questions: ", prompt)
    print("Llama Questions: ", response)
    print("-"*50)

###########################################

new_message = {
    "role": "user", 
    "content": "You have now seen many different types of questions. Form 10 questions on similar topics. Questions do not have to be exactly the same topic range, you can ask something similar but beyond the scope. Please keep the question concise and clear."
}

conversation_history.append(new_message)

response = ""

stream = ollama.chat(
    model="llama3.2",
    messages=conversation_history,
    stream=True
)

for chunk in stream:
    response += chunk["message"]["content"]

assistant_message = {
    "role": "assistant", 
    "content": response
}

conversation_history.append(assistant_message)
ollama_response.append(response)

print("#"*100)
print("New Questions: (By Llama 3.2)")
print(response)




