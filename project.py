# Listed in requirements.txt
import numpy as np

def main():
    user_amount = get_valid_amount("Loan Amount: ")
    rate = get_valid_rate("Annual Interest Rate (as a percentage): ")
    years = get_valid_amount("Number of Years: ")
    payment = get_valid_amount("Monthly Payment: ")

    # Calculate compound interest
    compound_interest = calculate_compound_interest(user_amount, rate, years)
    print(f"Compound Interest after {years} years: {compound_interest}")

    # Calculate future value
    periods = years * 12  # Assuming monthly investments/payments
    future_value = calculate_future_value(payment, rate / 12, periods)
    print(f"Future Value of Monthly Payments: {future_value}")

    # Calculate loan payment
    monthly_payment = calculate_loan_payment(user_amount, rate / 12, periods)
    print(f"Monthly Loan Payment: {monthly_payment}")

def calculate_compound_interest(principal, rate, years):
    """
    Calculate compound interest.

    """
    amount = principal * np.power(1 + rate, years)
    return format_currency(amount)

def calculate_future_value(payment, rate, periods):
    """
    Calculate the future value of regular investments.

    """

    future_value = payment * (np.power(1 + rate, periods) - 1) / rate  # Using numpy's power function
    return format_currency(future_value)

def calculate_loan_payment(principal, rate, periods):

    """
    Calculate the monthly loan payment.

    """
    payment = principal * (rate * np.power(1 + rate, periods)) / (np.power(1 + rate, periods) - 1)
    return format_currency(payment)

def get_valid_amount(prompt):
    while True:
        try:
            amount = float(input(prompt))
            if amount <= 0:
                print("Please enter a positive amount.")
            else:
                return amount
        except ValueError:
            print("Please enter a valid number.")

def get_valid_rate(prompt):
    while True:
        try:
            rate = float(input(prompt))
            if rate <= 0:
                print("Please enter a positive interest rate.")
            else:
                return rate / 100
        except ValueError:
            print("Please enter a valid number.")

def format_currency(value):
    return f"${value:.2f}"

if __name__ == "__main__":
    main()
