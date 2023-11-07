from llama_cpp import Llama
llm = Llama(model_path="llama-7b.ggmlv3.q4_0.bin")

response=llm("Share some cool facts about The Office TV Series.")
print(response['choices'][0]['text'])