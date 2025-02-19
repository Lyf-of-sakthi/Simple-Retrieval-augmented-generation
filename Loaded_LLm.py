from huggingface_hub import InferenceClient

api = InferenceClient(token="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")


def generate_answer(context, query):
    prompt = f"Context: {context}\nQuestion: {query}\nAnswer:"
    response = api.text_generation(model="tiiuae/falcon-7b-instruct", prompt=prompt)
    return response


'''from huggingface_hub import InferenceClient

api = InferenceClient(token="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")

response = api.text_generation(model="tiiuae/falcon-7b-instruct", prompt="What colour is your bugatti da ?")
print(response)


from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = "tiiuae/falcon-7b-instruct"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

input_text = "hi, I am Sakthi."
inputs = tokenizer(input_text, return_tensors="pt")
outputs = model.generate(**inputs, max_length=100)
print(tokenizer.decode(outputs[0], skip_special_tokens=True))'''

