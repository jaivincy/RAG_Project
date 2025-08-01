from litellm import completion
from pydantic import BaseModel
import json

class identifier(BaseModel):
    is_news: bool
    is_weather: bool
    is_location: str

question=input("Enter the question:")

response=completion(
    model="ollama/llama3.2:3b",
    messages=[
        {"role":"system","content":(
            "you are an expert classsifier.given a user's question respond ONLY with a JSON object in this formate:\n"
            "{\n"
            ' "is_news":true/false,\n'
            ' "is_weather":true/false,\n'
            "}\n"
            "guidelines:\n
            "- set is_news to true if the question is about current events,news,or recent happenings (for example:'what happen in madurai').\n"
            "- set is_weather to true if the question is about weather conditions,temperature,rainfall,or climate (for example:'what is the weather in madurai').\n"
            "- set is_location to true if the question is about a specific location or place (for example:'what is the weather in madurai').\n"
            do not include and explanation 
        )}
    ]