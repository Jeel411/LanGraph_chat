from dotenv import load_dotenv
load_dotenv()

from langchain.chat_models import init_chat_model       #this is universal helper for chatmodels
from langchain_groq import ChatGroq                     #this is provider specific 

llm = init_chat_model("groq:qwen/qwen3.8-27b")  

print(llm.invoke("president of america as of 2026?").text)

from typing import TypedDict

class State(TypedDict):
    messages: list

def chatbot(state:State) ->State:
    return {"messages": [llm.invoke(state["message"])]}

from langgraph.graph import StateGraph, START, END

builder = StateGraph(State)
builder.add_node("chatbot_node", chatbot)
builder.add_edge(START, "chatbot_node")
builder.add_edge("chatbot_node", END)

graph=builder.compile()

#with open("llm.png", "wb") as f:
message = {"role": "user", "content":" who is PM of india?"}
print(graph.invoke({"messages":[message]}))

