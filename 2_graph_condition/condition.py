from typing import TypedDict, Literal

class pstate(TypedDict):        #creating class to specify data needed
    usd: float
    totalusd: float
    target_currency: Literal["INR", "EUR"]  #target variable has to be from specified string bcoz of literal
    total: float

#these are tools
def usreturn(state:pstate) -> pstate:
    state['totalusd'] = state['usd'] * 1.08
    return state

def convertinr(state:pstate) -> pstate:
    state["total"] = state["totalusd"]*85
    return pstate

def converteur(state:pstate) -> pstate:
    state["total"] = state["totalusd"] *0.9
    return pstate

def choosecurrency(state: pstate) -> pstate:
    return state["target_currency"]

#creating graph
from langgraph.graph import StateGraph, START, END
#creating node
builder = StateGraph(pstate)

#creating node
builder.add_node("usreturn_node", usreturn)
builder.add_node("convertinr_node", convertinr)
builder.add_node("converteur_node", converteur)

#creating paths/edges
builder.add_edge(START, "usreturn_node")
builder.add_conditional_edges("usreturn_node", choosecurrency, {
    "INR":"convertinr_node",
    "EUR":"converteur_node",
})
builder.add_edge(["convertinr_node","converteur_node"], END)

graph = builder.compile()
image=graph.get_graph().draw_mermaid_png()
with open("conditiona.png", "wb") as f:
    f.write(image)

graph.invoke({"usd":1000, "target_currency": "EUR"})