import streamlit as st
from utils.nqueens import run_nqueens_app
from utils.puzzle8 import run_8puzzle_app
from utils.pathfinder import run_pathfinder_app
from utils.knapsack import run_knapsack_app
from utils.scheduler import run_scheduler_app  # Ensure this line is included for Task Scheduler
from utils.travelroute import run_travelroute_app  # Ensure this line is included for TSP
from utils.currencyconverter import run_currencyconverter_app  # Ensure this line is included for Currency Converter
from utils.sudoku import run_sudoku_app  # Ensure this line is included for Sudoku Solver

# Set the page configuration with a custom page title
st.set_page_config(page_title="🔍 Real-Time Algorithmic Assistant", layout="wide")

# Main title displayed on the app
st.title("🤖 Real-Time Algorithmic Assistant")

# Sidebar for problem selection
problem = st.sidebar.selectbox("Choose a Problem to Explore", [
    "8-Puzzle Solver", 
    "N-Queens Problem", 
    "Pathfinding Maze", 
    "Knapsack (Zip Optimization)",
    "Task Scheduler",  # Add Task Scheduler option
    "Travel Route Planner (TSP)",  # Add Travel Route Planner option
    "Currency Converter",  # Add Currency Converter option
    "Sudoku Solver"  # Add Sudoku Solver option
])

if problem == "8-Puzzle Solver":
    run_8puzzle_app()
elif problem == "N-Queens Problem":
    run_nqueens_app()
elif problem == "Pathfinding Maze":
    run_pathfinder_app()
elif problem == "Knapsack (Zip Optimization)":
    run_knapsack_app()
elif problem == "Task Scheduler":  # Handle Task Scheduler
    run_scheduler_app()
elif problem == "Travel Route Planner (TSP)":  # Handle TSP
    run_travelroute_app()
elif problem == "Currency Converter":  # Handle Currency Converter
    run_currencyconverter_app()
elif problem == "Sudoku Solver":  # Handle Sudoku Solver
    run_sudoku_app()
