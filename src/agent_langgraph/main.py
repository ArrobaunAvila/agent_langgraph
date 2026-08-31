# pip install -U langgraph
# pip install -qU langchain "langchain[openai]"  libreria para trabajar con langchain - langchain openai
# pip install langgraph-cli    Libreria para debuggear nuestras orquestaciones de agentes
# pip install -qU langchain-ollama Instalacion de modelo gratuito en local (Ollama)

from langchain.agents import create_agent
from langchain_ollama import ChatOllama
from dotenv import load_dotenv


load_dotenv()

def get_weather(city: str) -> str:
    """Get weather for a given city."""
    return f"It's always sunny in {city}!"

model = ChatOllama(model="qwen2.5:3b")    

agent = create_agent(
    model=model,
    tools=[get_weather],
    system_prompt="You are a helpful assistant!",
)


