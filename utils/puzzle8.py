import streamlit as st
import heapq

# Goal state for the 8-puzzle
goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

# Heuristic: Manhattan Distance
def manhattan(state):
    distance = 0
    for i in range(3):
        for j in range(3):
            val = state[i][j]
            if val != 0:
                goal_x = (val - 1) // 3
                goal_y = (val - 1) % 3
                distance += abs(goal_x - i) + abs(goal_y - j)
    return distance

# Find zero position
def find_zero(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

# Generate valid neighbors
def get_neighbors(state):
    x, y = find_zero(state)
    neighbors = []
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = [row[:] for row in state]
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            neighbors.append(new_state)
    return neighbors

# Check if two states are the same
def same(s1, s2):
    return all(s1[i][j] == s2[i][j] for i in range(3) for j in range(3))

# A* Solver
def solve_puzzle(start):
    queue = [(manhattan(start), 0, start, [])]
    visited = set()

    while queue:
        est_total, cost, state, path = heapq.heappop(queue)
        state_tuple = tuple(tuple(row) for row in state)
        if state_tuple in visited:
            continue
        visited.add(state_tuple)

        if same(state, goal_state):
            return path + [state]

        for neighbor in get_neighbors(state):
            heapq.heappush(queue, (
                cost + 1 + manhattan(neighbor),
                cost + 1,
                neighbor,
                path + [state]
            ))
    return []

# Streamlit UI
def run_8puzzle_app():
    st.set_page_config(page_title="8-Puzzle Solver", layout="centered")
    st.title("🧩 8-Puzzle Solver")
    st.markdown("""
    A real-time solver for the 8-tile sliding puzzle using **A\*** Search algorithm.  
    **Heuristic:** Manhattan Distance  
    Try rearranging the puzzle to see the solution path.
    ---
    """)

    default = [[1, 2, 3], [4, 0, 6], [7, 5, 8]]
    user_input = []

    st.markdown("### 🔢 Enter Puzzle State (comma-separated):")
    for i in range(3):
        row = st.text_input(f"Row {i+1}", value=",".join(map(str, default[i])), key=f"r{i}")
        try:
            values = list(map(int, row.strip().split(',')))
            if len(values) != 3 or not all(0 <= v <= 8 for v in values):
                st.error(f"⚠️ Row {i+1} must have 3 values (0–8).")
                return
            user_input.append(values)
        except:
            st.error(f"❌ Invalid input in row {i+1}.")
            return

    flat = sum(user_input, [])
    if len(set(flat)) != 9:
        st.error("⚠️ Puzzle must contain unique numbers from 0 to 8.")
        return

    if st.button("🧠 Solve Puzzle"):
        with st.spinner("Solving..."):
            solution = solve_puzzle(user_input)
        if not solution:
            st.error("🚫 No solution found. Try a different configuration.")
        else:
            st.success(f"✅ Solved in {len(solution)-1} moves!")
            for idx, state in enumerate(solution):
                st.markdown(f"**Step {idx}**")
                st.table(state)
