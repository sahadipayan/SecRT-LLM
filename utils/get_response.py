import openai

openai.api_key = open(r"api_key.txt", "r").read().strip("\n")

def get_response(prompt, model, temperature):
    
    completion = openai.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        temperature=temperature,
    )
    return completion.choices[0].message.content.strip()

