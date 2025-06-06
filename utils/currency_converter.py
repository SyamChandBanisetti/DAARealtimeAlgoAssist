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
    st.set_page_config(page_title="💵 Currency Change Maker", layout="centered")
    st.title("💰 Currency Change Maker")
    st.markdown(
        """
        Welcome to the **Currency Change Maker**!  
        Enter your available coin/note denominations and a target amount.  
        We'll compute the **minimum number of coins/notes** required using **Dynamic Programming**.
        ---
        """
    )

    st.subheader("🪙 Enter Denominations")
    with st.expander("How to enter denominations?"):
        st.write(
            """
            - Enter positive integers separated by commas (e.g. `1, 2, 5, 10`)  
            - Denominations will be sorted and duplicates removed automatically  
            - Example: Indian currency notes and coins: `1, 2, 5, 10, 20, 50, 100, 200, 500, 2000`
            """
        )

    # Use a text input for denominations
    coin_input = st.text_input("Your coin/note values (comma-separated):", value="1, 2, 5, 10, 20, 50, 100")

    # Parse coins with validation
    try:
        coins = list(map(int, coin_input.strip().split(',')))
        coins = sorted(set([c for c in coins if c > 0]))
        if not coins:
            raise ValueError("No valid denominations found.")
        coins_str = ", ".join(f"₹{c}" for c in coins)
    except Exception:
        st.error("⚠️ Please enter valid positive integers for denominations.")
        return

    st.markdown(f"**Available denominations:** {coins_str}")

    # Amount input with a slider and number input combined in columns for better UX
    st.subheader("💵 Enter Amount to Make Change For")
    col1, col2 = st.columns([3, 1])
    with col1:
        amount = st.number_input("Amount (₹):", min_value=1, value=57, step=1)
    with col2:
        calculate = st.button("💸 Calculate Minimum Coins")

    if calculate:
        count, used = min_coins(coins, amount)
        if count == -1:
            st.error("❌ Cannot make this amount with the given denominations.")
        else:
            st.success(f"✅ Minimum Coins/Notes Required: **{count}**")

            # Count coins used
            coin_count = {}
            for coin in used:
                coin_count[coin] = coin_count.get(coin, 0) + 1

            st.subheader("📦 Coins/Notes Breakdown")
            # Nicely display coin counts with emojis and better formatting
            for coin in sorted(coin_count.keys(), reverse=True):
                qty = coin_count[coin]
                # Use different emojis for coins and notes
                emoji = "🪙" if coin <= 10 else "💵"
                st.markdown(f"{emoji}  ₹**{coin}** × **{qty}**")

    st.markdown("---")
    st.caption("🔁 Built using dynamic programming for efficient and optimal solutions.")

if __name__ == "__main__":
    run_change_maker_app()
