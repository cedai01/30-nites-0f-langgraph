from typing import TypedDict
from langgraph.graph import StateGraph, START, END
import random

class GameState(TypedDict):
    player: str
    computer: str
    result: str

def player_choice(state: GameState) -> GameState:
    # just keep the player's choice as is
    return state

def computer_choice(state: GameState) -> GameState:
    choices = ["rock", "paper", "scissors"]
    state["computer"] = random.choice(choices)
    return state

def determine_winner(state: GameState) -> GameState:
    p, c = state["player"], state["computer"]

    if p == c:
        state["result"] = "draw"
    elif (p == "rock" and c == "scissors"):
        state["result"] = "player_rock_win"
    elif (p == "paper" and c == "rock"):
        state["result"] = "player_paper_win"
    elif (p == "scissors" and c == "paper"):
        state["result"] = "player_scissors_win"
    elif (c == "rock" and p == "scissors"):
        state["result"] = "computer_rock_win"
    elif (c == "paper" and p == "rock"):
        state["result"] = "computer_paper_win"
    elif (c == "scissors" and p == "paper"):
        state["result"] = "computer_scissors_win"
    else:
        state["result"] = "invalid"
    return state

def results(state: GameState) -> GameState:
    print(f"You chose {state['player']}, Computer chose {state['computer']}")
    print("Result:", state["result"])
    return state

# Build graph
graph = StateGraph(GameState)
graph.add_node("player_choice", player_choice)
graph.add_node("computer_choice", computer_choice)
graph.add_node("determine_winner", determine_winner)
graph.add_node("results", results)

graph.add_edge(START, "player_choice")
graph.add_edge("player_choice", "computer_choice")
graph.add_edge("computer_choice", "determine_winner")
graph.add_edge("determine_winner", "results")
graph.add_edge("results", END)

app = graph.compile()

# Run
user_input = input("Enter your choice (rock, paper, scissors): ").strip().lower()
app.invoke({"player": user_input, "computer": "", "result": ""})

