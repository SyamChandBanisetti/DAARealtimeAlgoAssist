import streamlit as st

# Import the individual algorithm functions from the utils folder
from utils.puzzle8 import run_8puzzle_app
from utils.nqueens import run_nqueens_app
from utils.pathfinder import run_pathfinder_app
from utils.knapsack import run_knapsack_app
from utils.scheduler import run_scheduler_app
from utils.travel_route import run_travel_route_app
from utils.currency_converter import run_currency_converter_app
from utils.sudoku_solver import run_sudoku_solver_app

# Set up the page config
st.set_page_config(page_title="🔍 Real-Time Algorithmic Assistant", layout="wide")

# Display main title
st.title("🤖 Real-Time Algorithmic Assistant")

# Sidebar for selecting problems
problem = st.sidebar.selectbox("Choose a Problem to Explore", [
    "8-Puzzle Solver", 
    "N-Queens Problem", 
    "Pathfinding Maze", 
    "Knapsack (Zip Optimization)",
    "Task Scheduler",
    "Travel Route Planner (TSP)",
    "Currency Converter",
    "Sudoku Solver"
])

# Run the corresponding app based on user selection
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
    run_travel_route_app()
elif problem == "Currency Converter":
    run_currency_converter_app()
elif problem == "Sudoku Solver":
    run_sudoku_solver_app()
