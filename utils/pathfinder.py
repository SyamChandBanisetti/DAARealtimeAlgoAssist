import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# DFS Algorithm
def dfs(grid, start, end, visited=None, path=None):
    if visited is None: visited = set()
    if path is None: path = []
    if start == end:
        return path + [end]
    x, y = start
    visited.add((x, y))
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == 0 and (nx, ny) not in visited:
            result = dfs(grid, (nx, ny), end, visited, path + [start])
            if result:
                return result
    return []

# Draw maze with path
def display_maze(grid, path):
    rows, cols = grid.shape
    fig, ax = plt.subplots(figsize=(cols / 2, rows / 2))
    for i in range(rows):
        for j in range(cols):
            color = 'green' if (i, j) in path else ('black' if grid[i][j] == 1 else 'white')
            rect = plt.Rectangle((j, rows - i - 1), 1, 1, facecolor=color, edgecolor='gray')
            ax.add_patch(rect)
    ax.set_xlim(0, cols)
    ax.set_ylim(0, rows)
    ax.set_aspect('equal')
    ax.axis('off')
    return fig

# Streamlit App
def run_pathfinder_app():
    st.set_page_config(page_title="DFS Maze Pathfinder", layout="centered")
    st.title("🧭 Maze Pathfinding using DFS")
    
    st.markdown("""
    This tool visualizes the path from a **start** to an **end** point in a grid-based maze using  
    **Depth-First Search (DFS)** algorithm.
    
    ---

    **Use Cases**:
    - 🤖 Robot navigation  
    - 🎮 Game AI  
    - 🌐 Network routing
    """)

    rows = st.slider("🔢 Number of Rows", 5, 20, 10)
    cols = st.slider("🔢 Number of Columns", 5, 20, 10)

    st.markdown("### 🧱 Define Your Maze")
    st.caption("Enter 0 for empty cell, 1 for wall — comma-separated per row:")

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
                return

            path = dfs(grid, (sx, sy), (ex, ey))
            if path:
                st.success(f"✅ Path found with {len(path)} steps!")
                fig = display_maze(grid, path)
                st.pyplot(fig)
            else:
                st.error("🚫 No path found. Try changing the wall configuration.")
        except:
            st.error("⚠️ Invalid coordinates format. Use: row,col (e.g., 0,0)")

if __name__ == "__main__":
    run_pathfinder_app()
