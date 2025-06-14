import streamlit as st

# Matplotlib imports for plotting and animations
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.animation import FuncAnimation
import numpy as np

def knapsack(weights, values, capacity):
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(values[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]

    res = dp[n][capacity]
    w = capacity
    selected = []

    for i in range(n, 0, -1):
        if res <= 0:
            break
        if res != dp[i - 1][w]:
            selected.append(i - 1)
            res -= values[i - 1]
            w -= weights[i - 1]

    return dp[n][capacity], selected[::-1]

def plot_knapsack(weights, values, capacity, selected):
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.set_title("Knapsack Selected Items Visualization")
    ax.set_xlim(0, capacity)
    ax.set_ylim(0, max(values) * 1.5)
    ax.set_xlabel("Weight")
    ax.set_ylabel("Value")

    current_weight = 0
    for idx in selected:
        rect = patches.Rectangle((current_weight, 0), weights[idx], values[idx], linewidth=1,
                                 edgecolor='blue', facecolor='cyan', alpha=0.7)
        ax.add_patch(rect)
        ax.text(current_weight + weights[idx] / 2, values[idx] / 2, f"Item {idx+1}\nW:{weights[idx]}\nV:{values[idx]}",
                ha='center', va='center', fontsize=9, weight='bold')
        current_weight += weights[idx]

    # Draw capacity line
    ax.axvline(x=capacity, color='red', linestyle='--', label='Knapsack Capacity')
    ax.legend()

    return fig

def run_knapsack_app():
    st.set_page_config(page_title="🎒 Knapsack Optimizer", layout="centered")
    st.title("🎒 0/1 Knapsack Problem Solver")

    st.markdown("""
    **🔍 Problem Description:**  
    Given a list of items with **weights** and **values**, determine the maximum total value that can be obtained **without exceeding the knapsack capacity**.

    ---
    **📦 Real-World Use Cases:**
    - Budget allocation with limited funds
    - Travel packing with space constraints
    - Resource planning in supply chain
    - Asset selection for investments
    """)

    num_items = st.slider("🧮 Number of Items", min_value=1, max_value=20, value=4)

    st.subheader("🔢 Item Details")
    weights, values = [], []
    for i in range(num_items):
        cols = st.columns([1, 1])
        weight = cols[0].number_input(f"Item {i+1} Weight (kg)", min_value=1, value=1, key=f"w_{i}")
        value = cols[1].number_input(f"Item {i+1} Value (₹)", min_value=1, value=1, key=f"v_{i}")
        weights.append(weight)
        values.append(value)

    capacity = st.number_input("🎯 Knapsack Capacity (kg)", min_value=1, value=10)

    if st.button("🚀 Solve Knapsack Problem"):
        max_value, selected = knapsack(weights, values, capacity)
        st.success(f"💰 Maximum Value Achievable: **₹{max_value}**")

        if selected:
            st.subheader("📋 Selected Items Breakdown")
            for idx in selected:
                st.markdown(f"- **Item {idx + 1}** → 🏋️ Weight: **{weights[idx]} kg**, 💵 Value: **₹{values[idx]}**")

            fig = plot_knapsack(weights, values, capacity, selected)
            st.pyplot(fig)
        else:
            st.warning("⚠️ No items were selected. Try adjusting item weights or increasing the knapsack capacity.")

    st.markdown("---")
    st.caption("✅ Built with Dynamic Programming | By Syam Chand")

if __name__ == "__main__":
    run_knapsack_app()
