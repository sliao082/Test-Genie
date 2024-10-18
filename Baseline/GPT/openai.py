from openai import OpenAI
import os

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

prompt = "Please tell me where UIUC locates at?"

# check available models
# models = client.models.list()
# for model in models.data:
#     print(model)

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are an assistant that answers questions in college level."},
        {"role": "user", "content": prompt}
    ],
    max_tokens=10,
)

# print(response.choices[0].message["content"].strip())



