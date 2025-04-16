import streamlit as st

def knapsack(weights, values, capacity):
    n = len(weights)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i-1] <= w:
                dp[i][w] = max(values[i-1] + dp[i-1][w - weights[i-1]], dp[i-1][w])
            else:
                dp[i][w] = dp[i-1][w]
    
    res = dp[n][capacity]
    w = capacity
    items_selected = []
    
    for i in range(n, 0, -1):
        if res <= 0:
            break
        if res != dp[i-1][w]:
            items_selected.append(i-1)
            res -= values[i-1]
            w -= weights[i-1]
    
    return dp[n][capacity], items_selected[::-1]

def run_knapsack_app():
    st.header("🎒 Knapsack Optimization (0/1 Knapsack)")
    st.markdown("""
    **Real-World Use Cases**:
    - Budget allocation
    - Backpack packing optimization
    - Resource distribution in logistics
    - Investment portfolio planning

    ✅ Solved using **Dynamic Programming**
    """)

    num_items = st.number_input("Number of Items", min_value=1, max_value=20, value=4)
    weights = []
    values = []

    st.subheader("📦 Item Details")
    for i in range(num_items):
        col1, col2 = st.columns(2)
        with col1:
            w = st.number_input(f"Item {i+1} Weight", min_value=1, value=1, key=f"w{i}")
        with col2:
            v = st.number_input(f"Item {i+1} Value", min_value=1, value=1, key=f"v{i}")
        weights.append(w)
        values.append(v)

    capacity = st.number_input("🎯 Knapsack Capacity", min_value=1, value=10)

    if st.button("🧠 Solve Knapsack"):
        max_value, selected_indices = knapsack(weights, values, capacity)
        st.success(f"✅ Maximum Value: {max_value}")
        if selected_indices:
            st.markdown("### Items Selected:")
            for idx in selected_indices:
                st.write(f"• Item {idx+1}: Weight = {weights[idx]}, Value = {values[idx]}")
        else:
            st.warning("No items selected. Try increasing capacity or adjusting values.")
