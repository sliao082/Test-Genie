''' 
    Llama 3.2 - 3B: /Users/sanhorn/.llama/checkpoints/Llama3.2-3B 
    Llama 3.1 - 405B: /Users/sanhorn/.llama/checkpoints/Llama3.1-405B/checklist.chk
'''
path_llama3_2_3b = "/Users/sanhorn/.llama/checkpoints/Llama3.2-3B"

# from transformers import LlamaTokenizer, LlamaForCausalLM
# import torch

# tokenizer = LlamaTokenizer.from_pretrained(path_llama3_2_3b)
# model = LlamaForCausalLM.from_pretrained(path_llama3_2_3b)

# prompt = "Where is UIUC?"

# device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
# model.to(device)

# inputs = tokenizer(prompt, return_tensors="pt").to(device)

# # Generate text
# output = model.generate(inputs['input_ids'], max_length=50)

# # Decode and print the generated text
# generated_text = tokenizer.decode(output[0], skip_special_tokens=True)
# print(generated_text)

from transformers import AutoTokenizer, AutoModelForCausalLM

# Load tokenizer and model
# tokenizer = AutoTokenizer.from_pretrained("meta-llama/Llama-3.1-8B")
# model = AutoModelForCausalLM.from_pretrained("meta-llama/Llama-3.1-8B")
# # Check if pad_token_id is set; if not, set it to eos_token_id
# if tokenizer.pad_token_id is None:
#     tokenizer.pad_token_id = tokenizer.eos_token_id

# # Define prompt and encode with attention mask
# prompt = "Where is UIUC"
# inputs = tokenizer(prompt, return_tensors="pt", padding=True)
# inputs['attention_mask'] = inputs['input_ids'].ne(tokenizer.pad_token_id)  # Set attention mask

# # Generate output with pad_token_id set
# output = model.generate(
#     inputs["input_ids"],
#     max_length=50,
#     attention_mask=inputs['attention_mask'],
#     pad_token_id=tokenizer.pad_token_id  # Set pad_token_id explicitly
# )

# # Decode and print the generated text
# generated_text = tokenizer.decode(output[0], skip_special_tokens=True)
# print(generated_text)

import transformers
import torch

model_id = "meta-llama/Llama-3.1-8B"

pipeline = transformers.pipeline(
    "text-generation", model=model_id, model_kwargs={"torch_dtype": torch.bfloat16}, device_map="auto"
)

pipeline("Hey how are you doing today?")