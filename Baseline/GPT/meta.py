''' 
    Llama 3.2 - 3B: /Users/sanhorn/.llama/checkpoints/Llama3.2-3B 
    Llama 3.1 - 405B: /Users/sanhorn/.llama/checkpoints/Llama3.1-405B/checklist.chk
'''
path_llama3_2_3b = "/Users/sanhorn/.llama/checkpoints/Llama3.2-3B"

from transformers import LlamaTokenizer, LlamaForCausalLM
import torch

tokenizer = LlamaTokenizer.from_pretrained(path_llama3_2_3b)
model = LlamaForCausalLM.from_pretrained(path_llama3_2_3b)

prompt = "Where is UIUC?"

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

inputs = tokenizer(prompt, return_tensors="pt").to(device)

# Generate text
output = model.generate(inputs['input_ids'], max_length=50)

# Decode and print the generated text
generated_text = tokenizer.decode(output[0], skip_special_tokens=True)
print(generated_text)
