# rent_vs_own_calculator.py

import streamlit as st

def calculate_buying_costs(purchase_price, annual_interest_rate, years_stay, zip_code):
    # Calculate mortgage payments
    monthly_interest_rate = annual_interest_rate / 12
    num_payments = years_stay * 12
    mortgage_payment = (purchase_price * monthly_interest_rate) / (1 - (1 + monthly_interest_rate) ** -num_payments)

    # Other costs (property taxes, insurance, maintenance, etc.)
    # Add your own calculations here based on user input

    return mortgage_payment

def main():
    st.title("Rent vs. Buy Calculator")

    # Collect user inputs
    purchase_price = st.number_input("Purchase Price ($)", min_value=1)
    annual_interest_rate = st.slider("Annual Interest Rate (%)", min_value=0.0, max_value=10.0, step=0.1)
    years_stay = st.slider("Years You Plan to Stay", min_value=1, max_value=30)
    zip_code = st.text_input("Zip Code")

    # Calculate buying costs
    mortgage_payment = calculate_buying_costs(purchase_price, annual_interest_rate / 100, years_stay, zip_code)

    # Collect renting costs
    rent_cost = st.number_input("Monthly Rent ($)", min_value=1)
    rent_increase = st.slider("Yearly Rent Increase (%)", min_value=0.0, max_value=10.0, step=0.1)

    # Compare costs
    total_cost_buying = mortgage_payment * years_stay
    total_cost_renting = rent_cost * 12 * years_stay

    st.write(f"Monthly Mortgage Payment: ${mortgage_payment:.2f}")
    st.write(f"Total Cost of Buying: ${total_cost_buying:.2f}")
    st.write(f"Total Cost of Renting: ${total_cost_renting:.2f}")

    # Add more visualizations (e.g., breakeven point)

if __name__ == "__main__":
    main()
