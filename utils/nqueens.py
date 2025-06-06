import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def is_safe(board, row, col, n):
    for i in range(col):
        if board[row][i] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, n), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True

def solve_nqueens_util(board, col, n):
    if col >= n:
        return True
    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 1
            if solve_nqueens_util(board, col + 1, n):
                return True
            board[i][col] = 0
    return False

def solve_nqueens(n):
    board = [[0 for _ in range(n)] for _ in range(n)]
    if not solve_nqueens_util(board, 0, n):
        return None
    return board

def draw_board(board):
    n = len(board)
    fig, ax = plt.subplots(figsize=(6, 6))
    for i in range(n):
        for j in range(n):
            color = '#f0d9b5' if (i + j) % 2 == 0 else '#b58863'  # classic chessboard colors
            rect = plt.Rectangle((j, n - i - 1), 1, 1, facecolor=color)
            ax.add_patch(rect)
            if board[i][j] == 1:
                ax.text(j + 0.5, n - i - 1 + 0.5, "♛", fontsize=24, ha='center', va='center', color='black')
    ax.set_xlim(0, n)
    ax.set_ylim(0, n)
    ax.set_aspect('equal')
    ax.axis('off')
    return fig

def run_nqueens_app():
    st.set_page_config(page_title="♛ N-Queens Solver", layout="centered")
    st.title("♛ N-Queens Problem Solver")

    st.markdown("""
    The **N-Queens Problem** involves placing `N` queens on an `N x N` chessboard so that no two queens threaten each other.

    ---
    ✅ **Solving Method**: Backtracking  
    📌 **Constraints**:
    - Only one queen per row and column
    - No two queens can share the same diagonal

    🛠️ **Applications**:
    - Scheduling jobs or exams
    - Circuit design
    - Wireless channel allocation
    """)

    n = st.slider("🔢 Select the number of queens (N)", min_value=4, max_value=12, value=8)

    if st.button("🚀 Solve Now"):
        board = solve_nqueens(n)
        if board:
            st.success(f"✅ Successfully placed {n} queens without conflict!")
            fig = draw_board(board)
            st.pyplot(fig)
        else:
            st.error("❌ No solution exists for this configuration.")

    st.markdown("---")
    st.caption("💡 Try different values of N to explore multiple board sizes!")

if __name__ == "__main__":
    run_nqueens_app()
