import streamlit as st

def calculate_costs(home_price, down_payment, interest_rate, rental_cost):
    # Your cost calculations go here (e.g., mortgage payments, equity, taxes).
    # Return results.

def main():
    st.title("Rent vs. Buy Calculator")
    st.sidebar.header("User Inputs")

    home_price = st.sidebar.number_input("Home Price ($)", min_value=1)
    down_payment = st.sidebar.number_input("Down Payment ($)", min_value=0)
    interest_rate = st.sidebar.slider("Interest Rate (%)", 0.0, 10.0, 3.5)
    rental_cost = st.sidebar.number_input("Monthly Rent ($)", min_value=0)

    if st.sidebar.button("Calculate"):
        results = calculate_costs(home_price, down_payment, interest_rate, rental_cost)
        # Display results (e.g., total costs, equity, tax benefits).

if __name__ == "__main__":
    main()
