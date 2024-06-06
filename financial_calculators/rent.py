# rent_vs_own_calculator.py

import streamlit as st
import requests

def calculate_buying_costs(purchase_price, annual_interest_rate, years_stay, zip_code):
    # Calculate mortgage payments
    monthly_interest_rate = annual_interest_rate / 12
    num_payments = years_stay * 12
    mortgage_payment = (purchase_price * monthly_interest_rate) / (1 - (1 + monthly_interest_rate) ** -num_payments)

    # Other costs (property taxes, insurance, maintenance, etc.)
    # Add your own calculations here based on user input

    return mortgage_payment

def get_appreciation_rate(zip_code):
    # Fetch appreciation rate from a free API (replace with actual API)
    # Example: Using a placeholder value for demonstration
    appreciation_rate = 0.05
    return appreciation_rate

def main():
    st.title("Rent vs. Buy Calculator")

    # Set default values
    default_purchase_price = 600000
    default_interest_rate = 3.5  # Average interest rate banks charge
    default_years_stay = 5
    default_rent_increase = 3.0

    # Collect user inputs
    purchase_price = st.number_input("Purchase Price ($)", min_value=1, value=default_purchase_price)
    annual_interest_rate = st.slider("Annual Interest Rate (%)", min_value=0.0, max_value=10.0, step=0.1, value=default_interest_rate)
    years_stay = st.slider("Years You Plan to Stay", min_value=1, max_value=30, value=default_years_stay)
    zip_code = st.text_input("Zip Code")

    # Calculate buying costs
    mortgage_payment = calculate_buying_costs(purchase_price, annual_interest_rate / 100, years_stay, zip_code)

    # Collect renting costs
    rent_cost = st.number_input("Monthly Rent ($)", min_value=1)
    rent_increase = st.slider("Yearly Rent Increase (%)", min_value=0.0, max_value=10.0, step=0.1, value=default_rent_increase)

    # Compare costs
    total_cost_buying = mortgage_payment * years_stay
    total_cost_renting = rent_cost * 12 * years_stay

    # Get appreciation rate
    appreciation_rate = get_appreciation_rate(zip_code)

    # Yearly breakdown table
    st.write("## Yearly Cost Breakdown")
    st.write(f"- Mortgage Payment: ${mortgage_payment:.2f} per month")
    st.write(f"- Property Taxes: ... (based on zip code)")
    # Add other costs here

    # Visual output (placeholder)
    st.write("## Cost Comparison Visualization")
    st.write(f"Appreciation Rate: {appreciation_rate * 100:.2f}%")
    # Add charts or graphs here

    # Conclusion
    if total_cost_buying < total_cost_renting:
        st.success("**Owning is better financially!**")
    else:
        st.error("**Renting is better financially!**")

if __name__ == "__main__":
    main()
