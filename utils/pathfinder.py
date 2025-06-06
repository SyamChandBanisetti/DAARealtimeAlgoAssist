import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.animation import FuncAnimation

# DFS with path exploration steps recorded for animation
def dfs_animated(grid, start, end):
    rows, cols = grid.shape
    visited = set()
    path = []
    steps = []  # To record explored cells at each recursion step

    def dfs_util(x, y):
        if not (0 <= x < rows and 0 <= y < cols):
            return False
        if grid[x][y] == 1 or (x, y) in visited:
            return False

        visited.add((x, y))
        path.append((x, y))
        steps.append(list(path))  # Record current path for animation

        if (x, y) == end:
            return True

        # Explore neighbors in 4 directions
        for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx, ny = x + dx, y + dy
            if dfs_util(nx, ny):
                return True

        path.pop()
        steps.append(list(path))  # Record backtrack step
        return False

    found = dfs_util(*start)
    return found, steps

def draw_cell(ax, x, y, cell_type):
    # cell_type: "wall", "road", "house", "start", "end", "path"
    colors = {
        "wall": "#444444",      # dark gray walls
        "road": "#F0F0F0",      # light gray roads (empty cells)
        "house": "#FFDDC1",     # peach houses
        "start": "#4CAF50",     # green start
        "end": "#E91E63",       # pink end
        "path": "#2196F3",      # blue path
        "visited": "#BBDEFB"    # light blue visited cells
    }
    rect = patches.Rectangle((y, x), 1, 1, linewidth=1, edgecolor="gray", facecolor=colors[cell_type])
    ax.add_patch(rect)

def display_maze_animation(grid, steps, start, end):
    rows, cols = grid.shape
    fig, ax = plt.subplots(figsize=(cols / 2, rows / 2))
    ax.set_xlim(0, cols)
    ax.set_ylim(0, rows)
    ax.set_aspect('equal')
    ax.axis('off')

    # Pre-draw houses randomly on some road cells for visual effect
    houses = set()
    np.random.seed(42)
    for i in range(rows):
        for j in range(cols):
            if grid[i, j] == 0 and np.random.rand() < 0.1:  # 10% chance of house on road
                houses.add((i, j))

    def init():
        ax.clear()
        ax.set_xlim(0, cols)
        ax.set_ylim(0, rows)
        ax.set_aspect('equal')
        ax.axis('off')
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    draw_cell(ax, i, j, "wall")
                elif (i, j) in houses:
                    draw_cell(ax, i, j, "house")
                else:
                    draw_cell(ax, i, j, "road")

        draw_cell(ax, *start, "start")
        draw_cell(ax, *end, "end")
        return []

    def update(frame):
        ax.clear()
        ax.set_xlim(0, cols)
        ax.set_ylim(0, rows)
        ax.set_aspect('equal')
        ax.axis('off')
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    draw_cell(ax, i, j, "wall")
                elif (i, j) in houses:
                    draw_cell(ax, i, j, "house")
                else:
                    draw_cell(ax, i, j, "road")

        draw_cell(ax, *start, "start")
        draw_cell(ax, *end, "end")

        visited_cells = set()
        for pos in steps[frame]:
            visited_cells.add(pos)

        # Draw visited but not in current path
        for cell in visited_cells:
            if cell != start and cell != end:
                draw_cell(ax, cell[0], cell[1], "visited")

        # Draw current path (last step in steps[frame])
        for cell in steps[frame]:
            if cell != start and cell != end:
                draw_cell(ax, cell[0], cell[1], "path")

        return []

    anim = FuncAnimation(fig, update, frames=len(steps), init_func=init, interval=250, repeat=False)

    return anim

# Streamlit App
def run_pathfinder_app():
    st.set_page_config(page_title="DFS Maze Pathfinder", layout="centered")
    st.title("🧭 Maze Pathfinding using DFS")

    st.markdown("""
    This tool visualizes the path from a **start** to an **end** point in a grid-based maze using  
    **Depth-First Search (DFS)** algorithm with animation.
    
    ---

    **Use Cases**:
    - 🤖 Robot navigation  
    - 🎮 Game AI  
    - 🌐 Network routing
    """)

    rows = st.slider("🔢 Number of Rows", 5, 20, 10)
    cols = st.slider("🔢 Number of Columns", 5, 20, 10)

    st.markdown("### 🧱 Define Your Maze")
    st.caption("Enter 0 for empty cell (road), 1 for wall — comma-separated per row:")

    grid = np.zeros((rows, cols), dtype=int)
    for i in range(rows):
        default_row = ",".join(["0"] * cols)
        row_input = st.text_input(f"Row {i+1}", value=default_row, key=f"row_{i}")
        try:
            row_values = list(map(int, row_input.strip().split(",")))
            if len(row_values) != cols:
                st.error(f"❌ Row {i+1} must have {cols} values.")
                return
            grid[i] = row_values
        except:
            st.error(f"❌ Invalid entry in Row {i+1}. Use 0 or 1 only.")
            return

    start = st.text_input("🚩 Start Position (row,col)", value="0,0")
    end = st.text_input("🏁 End Position (row,col)", value=f"{rows-1},{cols-1}")

    if st.button("🔍 Find Path"):
        try:
            sx, sy = map(int, start.strip().split(","))
            ex, ey = map(int, end.strip().split(","))

            if not (0 <= sx < rows and 0 <= sy < cols and 0 <= ex < rows and 0 <= ey < cols):
                st.error("⚠️ Start or end position is out of bounds.")
                return
            if grid[sx][sy] == 1 or grid[ex][ey] == 1:
                st.error("⚠️ Start or end point cannot be a wall (1).")
