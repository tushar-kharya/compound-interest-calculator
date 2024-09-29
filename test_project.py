# Listed in requirements.txt
import pytest
from project import calculate_compound_interest, calculate_future_value, calculate_loan_payment

def test_calculate_compound_interest():
    principal = 1000
    rate = 0.05
    years = 10
    result = calculate_compound_interest(principal, rate, years)
    assert result == "$1628.89"

def test_calculate_future_value():
    payment = 100
    rate = 0.05 / 12
    periods = 12 * 10
    result = calculate_future_value(payment, rate, periods)
    assert result == "$15528.23"

def test_calculate_loan_payment():
    principal = 5000
    rate = 0.04 / 12
    periods = 5 * 12
    result = calculate_loan_payment(principal, rate, periods)
    assert result == "$92.08"

if __name__ == "__main__":
    pytest.main()

