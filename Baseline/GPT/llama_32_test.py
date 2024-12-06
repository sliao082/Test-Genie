import ollama

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

def analyze_question_variety(questions):
    """
    Analyzes the variety of questions based on multiple factors
    """
    metrics = {
        "question_types": {
            "what": 0,
            "how": 0,
            "why": 0,
            "compare": 0,
            "analyze": 0,
            "explain": 0
        },
        "average_length": 0
    }
    
    for question in questions:
        question = question.lower().strip()
        if question:
            # Analyze question types
            if question.startswith('what'): metrics["question_types"]["what"] += 1
            elif question.startswith('how'): metrics["question_types"]["how"] += 1
            elif question.startswith('why'): metrics["question_types"]["why"] += 1
            elif 'compare' in question: metrics["question_types"]["compare"] += 1
            elif 'analyze' in question: metrics["question_types"]["analyze"] += 1
            elif 'explain' in question: metrics["question_types"]["explain"] += 1
            
            # Calculate average length
            metrics["average_length"] += len(question.split())
            
    if len(questions) > 0:
        metrics["average_length"] /= len(questions)
    
    return metrics

def set_mode(mode):
    return mode

def get_enhanced_system_prompt(mode):
    """
    Returns an enhanced system prompt that encourages question variety
    """
    return {
        "role": "system", 
        "content": f"""You are a helpful assistant forming new questions. You will be provided with sample test questions. Your job is to generate new test questions 
        on similar topics and areas through learning and referencing from the sample questions.
        Follow the guidelines to improve question variety:
        1. Generate questions across different cognitive levels (recall, understand, apply, analyze)
        2. Vary question formats (how, why, what-if, compare-contrast)
        3. Include real-world applications when possible
        4. Keep questions {mode} and concise
        5. Don't give out selections, just output the question
        6. Learn from sample questions but don't simply rephrase them
        7. Feel free to explore related topics while staying relevant"""
    }

def get_variety_feedback(metrics):
    """
    Generates feedback based on question variety metrics
    """
    feedback = []
    question_types = metrics["question_types"]
    
    # Check question type distribution
    feedback.append("Try to focus more on the topics as provided in the sample questions.")
    
    # Check question length
    if metrics["average_length"] < 10:
        feedback.append("Consider adding more context or details to questions")
    elif metrics["average_length"] > 30:
        feedback.append("Some questions might be too verbose")
        
    return feedback

# Main execution
file = "/Users/sanhorn/Desktop/UIUC/Junior/CS222/Test-Genie/Test/test3.txt"
test_questions, test_selections, test_answers = test_sparse(file)
mode = set_mode("easy")

# Initialize conversation with enhanced system prompt
conversation_history = [get_enhanced_system_prompt(mode)]

# Generate questions with variety tracking
ollama_response = []
for i, prompt in enumerate(test_questions):
    user_message = {
        "role": "user",
        "content": "Sample question to learn and reference from: " + prompt
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
    
    # Track response
    ollama_response.append(response)
    
    # Analyze variety and add feedback
    current_metrics = analyze_question_variety([response])
    variety_feedback = get_variety_feedback(current_metrics)
    
    feedback_message = {
        "role": "user", 
        "content": "For the next question: " + ". ".join(variety_feedback) + 
                   " Remember to explore related topics while maintaining the core subject matter."
    }
    conversation_history.append(feedback_message)

    print("Sample Question:", prompt)
    print("Generated Question:", response)
    print("Variety Feedback:", variety_feedback)
    print("-"*50)

# Generate final set of questions
new_message = {
    "role": "user", 
    "content": """Based on the sample questions seen, generate 10 diverse questions that:
    1. Cover different aspects of the topics
    2. Use varied question structures
    3. Include both theoretical and practical elements
    Please keep each question concise and clear."""
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

# Analyze final set of questions
final_metrics = analyze_question_variety(response.split('\n'))
final_feedback = get_variety_feedback(final_metrics)

print("#"*100)
print("Final Generated Questions:")
print(response)
print("\nVariety Analysis:")
print("Metrics:", final_metrics)
print("Feedback:", final_feedback)