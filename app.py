# app.py

import streamlit as st

# Import the individual algorithm app functions
from utils.puzzle8 import run_8puzzle_app
from utils.nqueens import run_nqueens_app
from utils.pathfinder import run_pathfinder_app
from utils.knapsack import run_knapsack_app
from utils.scheduler import run_scheduler_app
from utils.travel_route import run_tsp_app
from utils.currency_converter import run_change_maker_app
from utils.sudoku_solver import run_sudoku_solver_app

# Set up the Streamlit page configuration
st.set_page_config(
    page_title="🔍 Real-Time Algorithmic Assistant",
    layout="wide"
)

# App Title
st.title("🤖 Real-Time Algorithmic Assistant")
st.markdown("""
Welcome to your **all-in-one interactive algorithm playground**!  
Select a problem from the sidebar to visualize and solve real-world computational challenges.

---
""")

# Sidebar selection
problem = st.sidebar.selectbox("🧠 Choose a Problem to Explore", [
    "8-Puzzle Solver", 
    "N-Queens Problem", 
    "Pathfinding Maze", 
    "Knapsack (Zip Optimization)",
    "Task Scheduler",
    "Travel Route Planner (TSP)",
    "Currency Converter",
    "Sudoku Solver"
])

# Routing to selected algorithm app
if problem == "8-Puzzle Solver":
    run_8puzzle_app()
elif problem == "N-Queens Problem":
    run_nqueens_app()
elif problem == "Pathfinding Maze":
    run_pathfinder_app()
elif problem == "Knapsack (Zip Optimization)":
    run_knapsack_app()
elif problem == "Task Scheduler":
    run_scheduler_app()
elif problem == "Travel Route Planner (TSP)":
    run_tsp_app()
elif problem == "Currency Converter":
    run_change_maker_app()
elif problem == "Sudoku Solver":
    run_sudoku_solver_app()
