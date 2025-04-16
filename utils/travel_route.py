# utils/travel_route.py
import streamlit as st
import itertools

def calculate_total_distance(route, distances):
    total = 0
    for i in range(len(route)):
        total += distances[route[i - 1]][route[i]]
    return total

def solve_tsp_brute_force(distances):
    cities = list(range(len(distances)))
    min_distance = float('inf')
    best_route = []

    for perm in itertools.permutations(cities[1:]):  # Skipping the first city, i.e., City 1
        route = [0] + list(perm)
        dist = calculate_total_distance(route, distances)
        if dist < min_distance:
            min_distance = dist
            best_route = route
    return best_route, min_distance

def run_tsp_app():
    st.header("🚗 Travel Route Planner (TSP)")
    st.markdown("""
    This module finds the **shortest route** that visits each city exactly once and returns to the starting city.  
    Ideal for logistics, delivery paths, and travel optimization.
    """)

    n = st.slider("Number of Cities (Max 8)", 3, 8, 4)
    st.markdown("### Enter Distances Between Cities (Symmetric Matrix)")

    distances = []
    for i in range(n):
        row = st.text_input(f"Row {i+1} (comma-separated)", value=",".join(["0"] * n))
        distances.append(list(map(int, row.strip().split(','))))

    if st.button("🧠 Find Optimal Route"):
        try:
            best_route, min_distance = solve_tsp_brute_force(distances)
            city_names = [f"City {i+1}" for i in best_route]
            st.success(f"✅ Optimal Route: {' → '.join(city_names)} → City 1")
            st.write(f"📏 Total Distance: {min_distance}")
        except:
            st.error("❌ Please ensure distances are valid integers and matrix is correctly filled.")
