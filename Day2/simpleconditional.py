from typing import TypedDict
from langgraph.graph import StateGraph, START, END


class SimpleAgent(TypedDict):
    a: int
    b: int
    op: int
    result: int

def simple_conditional(state: SimpleAgent) -> SimpleAgent:
    """A simple node calculator That performs basic arithmetic calculations based on user input."""
    state["a"] = f"your first number to calculate is: {state["a"]} "
    state["b"] = f"your second number to calculate is: {state["b"]} "
    state["op"] = f"your operator to calculate is: {state["op"]} "
    state["result"] = f"result will be: {state["result"]} "

def calculate(state: SimpleAgent) -> SimpleAgent:
    """calculates the result from the user input"""
    if state["op"] == "+":
        state["result"] = state["a"] + state["b"]
    elif state["op"] == "-":
        state["result"] = state["a"] - state["b"]
    elif state["op"] == "*":
        state["result"] = state["a"] * state["b"]
    elif state["op"] == "/":
        if state["b"] == 0:
            print("Cannot divide by zero.")
            state["result"] = None
        else:
            state["result"] = state["a"] / state["b"]
    else:
        print("Invalid operator.")
        state["result"] = None
    
    return state


app = StateGraph(SimpleAgent)
app.add_node("simple_conditional", simple_conditional)
app.add_node("calculator", calculate)
app.add_edge(START, "calculator")
app.add_edge("calculator", "simple_conditional")
app.add_edge("simple_conditional", END)

graph = app.compile()

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
operator = input("Enter operator (+, -, *, /): ")

result = graph.invoke({"a": num1, "b": num2, "op": operator, "result": 0})

print(result["result"])