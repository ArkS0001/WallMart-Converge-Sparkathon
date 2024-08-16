# WALLMART

https://github.com/zheng-chong/catvton?tab=readme-ov-file#gradio-app

https://github.com/internlm/mindsearch           --shayd kaam aye prompt description

https://rapidapi.com/letscrape-6bRBa3QguO5/api/real-time-amazon-data/playground/apiendpoint_4c069629-23df-4946-aab8-a1cb41ba7862


# Use a pipeline as a high-level helper
from transformers import pipeline

pipe = pipeline("text-generation", model="meta-llama/Meta-Llama-3.1-405B")




# Load model directly
from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained("meta-llama/Meta-Llama-3.1-405B")
model = AutoModelForCausalLM.from_pretrained("meta-llama/Meta-Llama-3.1-405B")
