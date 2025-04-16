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
    Useful in banking systems, cash register algorithms, and coin vending systems.
    
    **Approach:**  
    We use **Dynamic Programming (DP)** to find the optimal solution for the given amount.  
    The idea is to iteratively compute the minimum number of coins required for each amount from 0 to the target amount.  
    At each step, we check whether including a coin will result in fewer coins than previously computed, ensuring an efficient solution.
    """)

    coin_input = st.text_input("Enter coin/note denominations (comma-separated)", value="1,2,5,10,20,50,100")
    coins = list(map(int, coin_input.strip().split(',')))
    amount = st.number_input("Enter the total amount to change", min_value=1, value=57)

    if st.button("💸 Get Minimum Coins"):
        count, used = min_coins(coins, amount)
        if count == -1:
            st.error("❌ Cannot make this amount with the given denominations.")
        else:
            st.success(f"✅ Minimum Coins/Notes Required: {count}")
            st.markdown("### Coins/Notes Used:")
            st.write(used)
