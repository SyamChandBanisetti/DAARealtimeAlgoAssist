# app.py
import streamlit as st
from utils.puzzle8 import run_8puzzle_app
from utils.nqueens import run_nqueens_app
from utils.pathfinder import run_pathfinder_app
from utils.knapsack import run_knapsack_app
from utils.scheduler import run_scheduler_app
from utils.tsp import run_tsp_app
from utils.change_maker import run_change_maker_app
from utils.sudoku import run_sudoku_app

st.set_page_config(page_title="🔍 Real-Time Algorithmic Assistant", layout="wide")
st.title("🤖 Real-Time Algorithmic Assistant")

st.sidebar.image("https://img.icons8.com/external-flatart-icons-flat-flatarticons/64/000000/artificial-intelligence.png", width=100)
problem = st.sidebar.selectbox("Select a Real-World Problem to Solve", [
    "8-Puzzle Solver",
    "N-Queens Visualizer",
    "Pathfinding Maze",
    "Knapsack Optimizer",
    "Task Scheduler",
    "Travel Route Planner (TSP)",
    "Currency Change Maker",
    "Sudoku Solver"
])

if problem == "8-Puzzle Solver":
    run_8puzzle_app()
elif problem == "N-Queens Visualizer":
    run_nqueens_app()
elif problem == "Pathfinding Maze":
    run_pathfinder_app()
elif problem == "Knapsack Optimizer":
    run_knapsack_app()
elif problem == "Task Scheduler":
    run_scheduler_app()
elif problem == "Travel Route Planner (TSP)":
    run_tsp_app()
elif problem == "Currency Change Maker":
    run_change_maker_app()
elif problem == "Sudoku Solver":
    run_sudoku_app()
