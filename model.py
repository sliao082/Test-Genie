# import torch
# from transformers import AutoTokenizer, FalconForCausalLM

# # Load tokenizer and model
# tokenizer = AutoTokenizer.from_pretrained("Rocketknight1/falcon-rw-1b")
# model = FalconForCausalLM.from_pretrained("Rocketknight1/falcon-rw-1b")

# # Tokenize input
# input_text = "Hello, my dog is cute."
# inputs = tokenizer(input_text, return_tensors="pt")

# # Generate a response (with improved configuration)
# outputs = model.generate(
#     **inputs, 
#     max_length=200,  # maximum number of tokens in the output
#     num_return_sequences=1,  # how many sequences to generate
#     no_repeat_ngram_size=2,  # prevents repetition of n-grams
#     pad_token_id=tokenizer.eos_token_id  # ensure eos_token is used for padding
# )

# # Decode the output token IDs to text
# response = tokenizer.decode(outputs[0], skip_special_tokens=True)
# # Print the response
# print(response)

from transformers import AutoTokenizer, AutoModelForCausalLM

# Load model and tokenizer
model = AutoModelForCausalLM.from_pretrained("google/gemma-2-2b")
tokenizer = AutoTokenizer.from_pretrained("google/gemma-2-2b")

# Input prompt
prompt = "How to effectively review for exams?"
inputs = tokenizer(prompt, return_tensors="pt")

# Generate a response with adjusted sampling parameters
outputs = model.generate(
    inputs.input_ids, 
    max_length=300, 
    do_sample=True, 
    temperature=0.7, 
    top_p=0.9,
    repetition_penalty=1.2
)

# Decode the response, skipping special tokens
response = tokenizer.decode(outputs[0], skip_special_tokens=True)
print(response)

