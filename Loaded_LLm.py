from huggingface_hub import InferenceClient
from transformers import AutoModelForCausalLM, AutoTokenizer
api = InferenceClient(token="Upload you huggingface token here")

def generate_answer(context, query):
    prompt = f"Context: {context}\nQuestion: {query}\nAnswer:"
    response = api.text_generation(model="tiiuae/falcon-7b-instruct", prompt=prompt)
    return response
