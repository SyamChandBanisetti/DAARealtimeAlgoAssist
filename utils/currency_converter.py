import streamlit as st

def min_coins(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    for coin in coins:
        for x in range(coin, amount + 1):
            dp[x] = min(dp[x], dp[x - coin] + 1)
    if dp[amount] == float('inf'):
        return -1, []
    
    result = []
    while amount > 0:
        for coin in coins:
            if amount - coin >= 0 and dp[amount - coin] == dp[amount] - 1:
                result.append(coin)
                amount -= coin
                break
    return dp[-1], result

def run_change_maker_app():
    st.header("💰 Currency Change Maker")
    st.markdown("""
    This tool helps compute the **minimum number of coins or notes** needed to make a given amount.  
    Useful in **banking systems, cash registers**, and **vending machines**.

    ---
    ### 🧠 Approach:
    We use **Dynamic Programming (DP)** to build up the optimal solution.
    
    For each sub-amount, we calculate the fewest coins needed and reuse those results to solve larger amounts efficiently.
    """)

    coin_input = st.text_input("Enter coin/note denominations (comma-separated)", value="1,2,5,10,20,50,100")
    try:
        coins = list(map(int, coin_input.strip().split(',')))
    except:
        st.error("⚠️ Please enter valid integers for coin denominations.")
        return

    amount = st.number_input("Enter the total amount to change", min_value=1, value=57)

    if st.button("💸 Get Minimum Coins"):
        count, used = min_coins(coins, amount)
        if count == -1:
            st.error("❌ Cannot make this amount with the given denominations.")
        else:
            st.success(f"✅ Minimum Coins/Notes Required: {count}")
            st.markdown("### 🪙 Coins/Notes Used:")

            # Count usage per denomination
            coin_count = {}
            for coin in used:
                coin_count[coin] = coin_count.get(coin, 0) + 1

            # Display sorted in descending order
            for coin in sorted(coin_count.keys(), reverse=True):
                st.markdown(f"• ₹{coin} × {coin_count[coin]}")
