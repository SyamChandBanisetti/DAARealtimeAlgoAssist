import streamlit as st

# Check if a number can be placed in given position
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

# Backtracking solver
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
    st.title("🧩 Sudoku Solver")
    st.markdown("""
    Enter your Sudoku puzzle below (use 0 for empty cells).  
    The solver uses **Backtracking** to find the solution.

    **Instructions:**  
    - Input exactly 9 rows.  
    - Each row must have 9 numbers separated by spaces (0-9).  
    - Use 0 for empty cells.
    """)

    board_input = []
    input_valid = True

    # Collect 9 rows of inputs in columns for better layout
    cols = st.columns(3)
    for i in range(9):
        col = cols[i % 3]
        row_str = col.text_input(f"Row {i+1}", "0 0 0 0 0 0 0 0 0", key=f"row{i}")
        try:
            row_vals = list(map(int, row_str.strip().split()))
            if len(row_vals) != 9 or any(n < 0 or n > 9 for n in row_vals):
                input_valid = False
                col.error("Each row must have exactly 9 numbers between 0 and 9.")
            board_input.append(row_vals)
        except Exception:
            input_valid = False
            col.error("Invalid input. Please enter numbers only.")

    if st.button("🚀 Solve Sudoku") and input_valid:
        board = [row[:] for row in board_input]  # copy input
        if solve_sudoku(board):
            st.success("✅ Sudoku Solved!")
            # Display solved board nicely
            st.markdown("### Solved Puzzle:")
            for row in board:
                st.write(" ".join(str(num) for num in row))
        else:
            st.error("❌ No solution exists for the given puzzle.")
    elif st.button("🚀 Solve Sudoku") and not input_valid:
        st.error("⚠️ Please fix input errors above before solving.")

