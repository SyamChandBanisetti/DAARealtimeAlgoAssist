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
    fig, ax = plt.subplots()
    for i in range(n):
        for j in range(n):
            color = 'white' if (i + j) % 2 == 0 else 'gray'
            rect = plt.Rectangle((j, n - i - 1), 1, 1, facecolor=color)
            ax.add_patch(rect)
            if board[i][j] == 1:
                ax.text(j + 0.5, n - i - 1 + 0.5, "♛", fontsize=20, ha='center', va='center', color='red')
    ax.set_xlim(0, n)
    ax.set_ylim(0, n)
    ax.set_aspect('equal')
    ax.axis('off')
    return fig

def run_nqueens_app():
    st.header("♛ N-Queens Solver (Backtracking)")
    st.markdown("""
    **Real-World Use**:
    - Used in job/task scheduling
    - Wireless channel allocation
    - Circuit layout optimization

    ✅ Solved using **Backtracking**
    """)

    n = st.slider("Select size of board (N)", min_value=4, max_value=12, value=8)

    if st.button("🧠 Solve N-Queens"):
        board = solve_nqueens(n)
        if board:
            st.success(f"✅ Successfully placed {n} queens!")
            fig = draw_board(board)
            st.pyplot(fig)
        else:
            st.error("❌ No solution found.")
