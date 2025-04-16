import streamlit as st

# Function to check if a number can be placed in the given position
def is_valid(board, row, col, num):
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False
    return True

# Backtracking function to solve Sudoku
def solve_sudoku(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if solve_sudoku(board):
                            return True
                        board[row][col] = 0
                return False
    return True

def run_sudoku_solver_app():
    st.header("🧩 Sudoku Solver")
    st.markdown("""
    This tool will solve a Sudoku puzzle using the **Backtracking Algorithm**.  
    You can enter a Sudoku puzzle, and it will return the solved puzzle in real-time.
    
    **Approach:**  
    The **Backtracking** approach tries each number (1-9) in an empty cell and recursively checks if the board remains valid.  
    If it finds a conflict, it backtracks and tries another number until the board is solved.
    """)

    board_input = []
    for i in range(9):
        row = st.text_input(f"Row {i + 1} (9 space-separated numbers, 0 for empty)", value="0 0 0 0 0 0 0 0 0")
        board_input.append(list(map(int, row.strip().split())))

    if st.button("🚀 Solve Sudoku"):
        if solve_sudoku(board_input):
            st.success("✅ Sudoku Solved!")
            st.write(board_input)
        else:
            st.error("❌ No solution exists for the given puzzle.")
