from typing import Dict, TypedDict
from langgraph.graph import StateGraph, START, END

class AgentState(TypedDict):
    """Simple agent state with a single message as a starting for my 30 nites of mastering langraph."""
    name: str

def compliment(state: AgentState) -> AgentState:
    """A simple function that compliments the user based on their message"""

    state["name"] = f"hello {state["name"]}! You are doing great! learning langraph is fun!"

    return state

graph = StateGraph(AgentState)

graph.add_node("complimenter", compliment)
graph.add_edge(START, "complimenter")
graph.add_edge("complimenter", END)

app = graph.compile()

result = app.invoke({"name": "Ced"})

print(result["name"])

