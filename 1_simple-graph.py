#graph based structure

from typing import TypedDict

class portfolioState(TypedDict):
    amount_us:float
    total_us:float
    total_inr:float

#creating object for our class
my_obj: portfolioState={'amount_us':100,'total_inr': 92.4,'total_us':89}

#this is node, inputing state and exporting state
def calc_total(state: portfolioState) -> portfolioState:
    state['total_us']=state['amount_us']*1.08
    return state

def conv_inr(state:portfolioState)-> portfolioState:       #state is name of object portfoliostate class
    state['total_inr'] = state['total_us']*85
    return state

#defining graph
from langgraph.graph import StateGraph, START, END
#this let us define graph
builder = StateGraph(portfolioState)

#adding nodes
builder.add_node("Total_node", calc_total)      #"this is name", for this function, which is converting to node
builder.add_node("conversion", conv_inr)

#chain type edges
builder.add_edge(START, "Total_node")
builder.add_edge("Total_node", "conversion")
builder.add_edge("conversion", END)

#display graph
#from IPython.display import Image, display
graph = builder.compile()
imag = graph.get_graph().draw_mermaid_png()

with open("graph.png", "wb") as f:      #saves image as graph.png
    f.write(imag)


graph.invoke({"amount_us":1000})