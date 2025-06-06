import streamlit as st
import itertools
import numpy as np

def calculate_total_distance(route, distances):
    total = 0
    for i in range(len(route)):
        total += distances[route[i - 1]][route[i]]
    total += distances[route[-1]][route[0]]  # return to start
    return total

def solve_tsp_brute_force(distances):
    cities = list(range(len(distances)))
    min_distance = float('inf')
    best_route = []

    for perm in itertools.permutations(cities[1:]):  # Fix city 0 as start
        route = [0] + list(perm)
        dist = calculate_total_distance(route, distances)
        if dist < min_distance:
            min_distance = dist
            best_route = route
    return best_route, min_distance

def run_tsp_app():
    st.title("🚗 Travel Route Planner (TSP)")
    st.markdown("""
    Find the **shortest route** visiting each city exactly once and returning to the starting city.  
    Useful for logistics, delivery optimization, and travel planning.

    **Instructions:**  
    - Select the number of cities (3 to 8).  
    - Enter distances between cities in the grid below (distance from City i to City j).  
    - Distance from a city to itself must be 0.  
    - Distances must be symmetric (distance from City i to City j equals City j to City i).
    """)

    n = st.slider("Number of Cities (Max 8)", 3, 8, 4)

    st.markdown("### Enter Distances Between Cities:")

    # Create an n x n numpy array to hold distances, initialized with zeros
    distances = np.zeros((n, n), dtype=int)

    # Input grid for distances
    cols = st.columns(n)
    for i in range(n):
        with st.container():
            row_cols = st.columns(n)
            for j in range(n):
                if i == j:
                    # Diagonal fixed to 0 and disabled input
                    distances[i][j] = 0
                    row_cols[j].number_input(
                        f"City {i+1}→City {j+1}", 
                        value=0, min_value=0, max_value=0, key=f"dist_{i}_{j}", disabled=True
                    )
                elif j < i:
                    # For lower triangle, mirror upper triangle input
                    distances[i][j] = distances[j][i]
                    row_cols[j].number_input(
                        f"City {i+1}→City {j+1}",
                        value=distances[i][j], min_value=0, max_value=10000, key=f"dist_{i}_{j}", disabled=True
                    )
                else:
                    # Upper triangle and off diagonal inputs
                    distances[i][j] = row_cols[j].number_input(
                        f"City {i+1}→City {j+1}",
                        value=distances[i][j], min_value=0, max_value=10000, key=f"dist_{i}_{j}"
                    )
                    # Mirror value to lower triangle to keep symmetric
                    distances[j][i] = distances[i][j]

    if st.button("🧠 Find Optimal Route"):
        # Validate distances array
        valid = True
        for i in range(n):
            if distances[i][i] != 0:
                st.error(f"Distance from City {i+1} to itself must be 0.")
                valid = False
            for j in range(n):
                if distances[i][j] != distances[j][i]:
                    st.error(f"Distances must be symmetric: distance[{i+1}, {j+1}] != distance[{j+1}, {i+1}]")
                    valid = False

        if not valid:
            st.stop()

        try:
            best_route, min_distance = solve_tsp_brute_force(distances)
            city_names = [f"City {i+1}" for i in best_route]
            st.success(f"✅ Optimal Route: {' → '.join(city_names)} → City 1")
            st.write(f"📏 Total Distance: {min_distance}")
        except Exception as e:
            st.error(f"❌ Error solving TSP: {e}")

if __name__ == "__main__":
    run_tsp_app()
