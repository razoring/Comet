from httpx import __name
from ollama import chat, ChatResponse, Client
import argparse

def main():
    client = Client()
    #print(client.list())
    models = sorted(client.list().models, key=lambda m:m.size, reverse=False)

    response:ChatResponse = chat(model=models[0].model, messages=[{"role":"system", "message":"You are an assistant."},{"role":"user", "message":"Hello World!"}], think=False, keep_alive=0)
    print(response.message.content)

if __name__ == "__main__": main()