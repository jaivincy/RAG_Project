from litellm import completion

response = completion(
    model="ollama/llama3.2:3b", 
    messages=[{ "content": "respond in 20 words. who is jaivincy?","role": "user"}], 
    api_base="http://localhost:11434",
    stream=True
)
for chunk in response:
    print(chunk['choices'][0]['delta']['content'],end ='',flush=True)