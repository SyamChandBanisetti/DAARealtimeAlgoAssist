import streamlit as st
import heapq

goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

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

def find_zero(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

def get_neighbors(state):
    x, y = find_zero(state)
    neighbors = []
    for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = [row[:] for row in state]
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            neighbors.append(new_state)
    return neighbors

def same(s1, s2):
    return all(s1[i][j] == s2[i][j] for i in range(3) for j in range(3))

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

def run_8puzzle_app():
    st.header("🧩 Real-Time 8-Puzzle Solver")
    st.markdown(\"\"\"
    **How it works**: Rearrange the tiles to reach the goal configuration using the empty space.
    
    ✅ Solved using **A\* Search**  
    📍 Heuristic: **Manhattan Distance**
    \"\"\")

    default = [[1, 2, 3], [4, 0, 6], [7, 5, 8]]
    st.markdown("### Input your 3x3 puzzle (comma-separated values):")
    user_input = []
    for i in range(3):
        row = st.text_input(f"Row {i+1}", value=','.join(map(str, default[i])))
        try:
            user_input.append(list(map(int, row.strip().split(','))))
        except:
            st.error("Enter valid integers for the puzzle.")
            return

    if st.button("🧠 Solve Puzzle"):
        with st.spinner("Solving..."):
            solution = solve_puzzle(user_input)
        if not solution:
            st.error("❌ No solution found. Try a solvable configuration.")
        else:
            st.success(f"✅ Puzzle Solved in {len(solution) - 1} moves!")
            for idx, state in enumerate(solution):
                st.markdown(f"**Step {idx}**")
                st.table(state)
