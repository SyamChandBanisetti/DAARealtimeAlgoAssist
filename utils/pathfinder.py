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
    for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == 0 and (nx, ny) not in visited:
            result = dfs(grid, (nx, ny), end, visited, path + [start])
            if result:
                return result
    return []

# Display the maze with path
def display_maze(grid, path):
    rows, cols = grid.shape
    fig, ax = plt.subplots()
    for i in range(rows):
        for j in range(cols):
            if (i, j) in path:
                color = 'green'
            elif grid[i][j] == 1:
                color = 'black'
            else:
                color = 'white'
            rect = plt.Rectangle([j, rows - i - 1], 1, 1, facecolor=color, edgecolor='gray')
            ax.add_patch(rect)
    ax.set_xlim(0, cols)
    ax.set_ylim(0, rows)
    ax.set_aspect('equal')
    ax.axis('off')
    return fig

def run_pathfinder_app():
    st.header("🧭 Pathfinding Maze (DFS Algorithm)")
    st.markdown("""
    **Real-World Use**:
    - Robot navigation in unknown environments
    - Game AI pathfinding
    - Network routing & GPS systems

    ✅ Solved using **Depth-First Search (DFS)**
    """)

    rows = st.slider("Rows", 5, 20, 10)
    cols = st.slider("Columns", 5, 20, 10)

    grid = np.zeros((rows, cols), dtype=int)

    st.markdown("#### Click to add walls (1 = wall, 0 = free):")
    for i in range(rows):
        row_vals = st.text_input(f"Row {i+1} (comma-separated, 0 or 1)", value=",".join(["0"] * cols))
        grid[i] = list(map(int, row_vals.strip().split(',')))

    start = st.text_input("Start Position (row,col)", value="0,0")
    end = st.text_input("End Position (row,col)", value=f"{rows-1},{cols-1}")

    if st.button("🧠 Find Path"):
        try:
            sx, sy = map(int, start.strip().split(','))
            ex, ey = map(int, end.strip().split(','))
            path = dfs(grid, (sx, sy), (ex, ey))
            if path:
                st.success(f"✅ Path found! Steps: {len(path)}")
                fig = display_maze(grid, path)
                st.pyplot(fig)
            else:
                st.error("❌ No path found. Try adjusting the maze.")
        except:
            st.error("⚠️ Invalid input. Please check coordinates.")
