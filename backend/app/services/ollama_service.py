import ollama

def get_summary_response_from_ollama(system_message_content, user_message_content, model):
    response = ""
    try:
        stream = ollama.chat(
            model=model,
            messages=[
                {"role": "system", "content": system_message_content},
                {"role": "user", "content": user_message_content}
            ],
            stream=True
        )

        for chunk in stream:
            response += chunk["message"]["content"]

    except Exception as e:
        print(f"An error occurred while communicating with the Ollama model: {e}")
        response = "There was an error processing the request."

    return response

def get_test_response_from_ollama(system_message_content, user_message_content, model):
    def analyze_question_variety(questions):
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
                if question.startswith('what'): metrics["question_types"]["what"] += 1
                elif question.startswith('how'): metrics["question_types"]["how"] += 1
                elif question.startswith('why'): metrics["question_types"]["why"] += 1
                elif 'compare' in question: metrics["question_types"]["compare"] += 1
                elif 'analyze' in question: metrics["question_types"]["analyze"] += 1
                elif 'explain' in question: metrics["question_types"]["explain"] += 1
                
                metrics["average_length"] += len(question.split())
                
        if len(questions) > 0:
            metrics["average_length"] /= len(questions)
        
        return metrics

    def set_mode(mode):
        return mode

    def get_enhanced_system_prompt(mode):
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
            7. Feel free to explore related topics while staying relevant
            8. Anything starts with Q: is a question, A: is an answer, S: is a selection"""
        }

    def get_variety_feedback(metrics):
        feedback = []
        question_types = metrics["question_types"]
        
        feedback.append("Try to focus more on the topics as provided in the sample questions.")
        
        if metrics["average_length"] < 10:
            feedback.append("Consider adding more context or details to questions")
        elif metrics["average_length"] > 30:
            feedback.append("Some questions might be too verbose")
            
        return feedback
    mode = set_mode("easy")
    conversation_history = [get_enhanced_system_prompt(mode)]
    ollama_response = []
    user_message = {
        "role": "user",
        "content": "Sample question to learn and reference from: " + user_message_content
    }
    conversation_history.append(user_message)

    response = ""
    stream = ollama.chat(
        model=model,
        messages=conversation_history,
        stream=True
    )
    
    for chunk in stream:
        response += chunk["message"]["content"]
    
    ollama_response.append(response)
    
    current_metrics = analyze_question_variety([response])
    variety_feedback = get_variety_feedback(current_metrics)
    
    feedback_message = {
        "role": "user", 
        "content": "For the next question: " + ". ".join(variety_feedback) + " Remember to explore related topics while maintaining the core subject matter."
    }
    conversation_history.append(feedback_message)

    new_message = {
        "role": "user", 
        "content": system_message_content
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

    return response