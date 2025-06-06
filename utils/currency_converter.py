# currency_converter.py

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
        for coin in sorted(coins, reverse=True):  # Prefer larger denominations
            if amount - coin >= 0 and dp[amount - coin] == dp[amount] - 1:
                result.append(coin)
                amount -= coin
                break
    return dp[-1], result

def run_change_maker_app():
    st.set_page_config(page_title="💵 Currency Converter", layout="centered")
    st.title("💰 Currency Change Maker")

    st.markdown("""
    Welcome to the **Currency Change Maker**!  
    Enter your available coin/note denominations and a target amount.  
    We'll compute the **minimum number of coins/notes** required using **Dynamic Programming**.

    ---
    """)

    st.subheader("🪙 Input Denominations")
    coin_input = st.text_input("Enter coin/note values (comma-separated):", value="1, 2, 5, 10, 20, 50, 100")

    try:
        coins = list(map(int, coin_input.strip().split(',')))
        coins = sorted(set([c for c in coins if c > 0]))
        if not coins:
            raise ValueError("No valid denominations found.")
    except Exception as e:
        st.error("⚠️ Please enter valid positive integers for denominations.")
        return

    amount = st.number_input("Enter the total amount to make change for:", min_value=1, value=57)

    if st.button("💸 Calculate Minimum Coins"):
        count, used = min_coins(coins, amount)
        if count == -1:
            st.error("❌ Cannot make this amount with the given denominations.")
        else:
            st.success(f"✅ Minimum Coins/Notes Required: {count}")

            coin_count = {}
            for coin in used:
                coin_count[coin] = coin_count.get(coin, 0) + 1

            st.subheader("📦 Coins/Notes Breakdown")
            for coin in sorted(coin_count.keys(), reverse=True):
                st.markdown(f"- ₹**{coin}** × **{coin_count[coin]}**")

    st.markdown("---")
    st.caption("🔁 Built using dynamic programming for efficient and optimal solutions.")

if __name__ == "__main__":
    run_change_maker_app()
