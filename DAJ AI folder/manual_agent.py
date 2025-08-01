from langchain_community.llms import Ollama
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
import re

# Initialize LLM
llm = Ollama(model="llama3.2:3b")
parser = StrOutputParser()

# Agent class with boolean checks and location extraction
class AgentAI:
    def __init__(self, user_query):
        self.query = user_query.lower()
        self.is_news = "news" in self.query
        self.is_weather = "weather" in self.query

        # Try to extract location (e.g., "weather in Chennai")
        location_match = re.search(r"(?:in|at|for)\s+([a-zA-Z\s]+)", self.query)
        self.location = location_match.group(1).strip() if location_match else "Tamil Nadu"

    def decide_agent(self):
        if self.is_news:
            return "news"
        elif self.is_weather:
            return "weather"
        else:
            return "unknown"

    def get_flags(self):
        return {
            "is_news": self.is_news,
            "is_weather": self.is_weather,
            "location": self.location
        }

# Templates
news_template = PromptTemplate.from_template("Give 3 short world news updates.")
weather_template = PromptTemplate.from_template("Simulate today's weather report in {location}.")

# Input from user
query = input(" Ask (just say 'news' or 'weather in <place>'): ")
agent = AgentAI(query)
agent_type = agent.decide_agent()
flags = agent.get_flags()

# Print boolean flags and location
print(f"\n Flags: {flags}")
print(f" Location: {agent.location}")

# Agent Response
if agent_type == "news":
    print("\n News Agent Activated:")
    chain = news_template | llm | parser
    print(chain.invoke({}))

elif agent_type == "weather":
    print(f"\n Weather Agent Activated for {agent.location}:")
    chain = weather_template | llm | parser
    print(chain.invoke({"location": agent.location}))

else:
    print("\n Only 'news' or 'weather' conditions are supported for now.")
