# Compound Interest Calculator

## Overview
Part of the CS50P final project, the **Compound Interest Calculator** is Python-based financial tool designed to help users perform essential financial calculations, such as calculating compound interest, determining the future value of regular investments, and computing the monthly payments needed to repay a loan. This project aims to empower users to make informed financial decisions by offering clear and accurate results.

## Highlights
- Developed core financial functions to handle compound interest, future value calculations, and loan repayment in Python.
- Ensured user-friendly input validation and output formatting, presenting results in a currency format for easy comprehension.
- Incorporated test-driven development (TDD) principles by implementing unit tests to verify the accuracy of each financial calculation function.

## Technologies Used
- **Python (NumPy)**: Mathematical operations for accurate financial calculations.
- **PyTest**: Unit testing framework for validating function accuracy.

## Data Analysis Workflow

1. **Core Functionalities**:
   - **Compound Interest Calculation**: Computes the total amount accumulated after a specified number of years, considering compound interest.
   - **Future Value Calculation**: Determines the future value of regular investments over a given period.
   - **Loan Repayment Calculation**: Calculates the fixed monthly payment required to repay a loan.

2. **Input Validation and Output Formatting**:
   - Implemented helper functions to ensure user inputs are valid (e.g., positive numbers, correct rate format).
   - Formatted numerical results as currency to improve readability.

3. **Testing**:
   - Used unit tests to validate key functions, ensuring accurate financial results:
     - **Compound Interest**: Verified against known values.
     - **Future Value**: Checked for regular investment accuracy.
     - **Loan Repayment**: Ensured correct monthly payment calculation.

## Presentation
A video demonstration of the Compound Interest Calculator, including how to use it and explanations of its core functionalities, can be found here:
- **[Video Demo](https://youtu.be/WpeMyAof-xw)**

## Files and Their Contents

1. **project.py** (Main Project File)
   - **Functions**:
     - `calculate_compound_interest(principal, rate, years)`: Calculates the total accumulated amount with compound interest.
     - `calculate_future_value(payment, rate, periods)`: Computes the future value of regular investments.
     - `calculate_loan_payment(principal, rate, periods)`: Determines the fixed monthly loan repayment amount.
     - `get_valid_amount(prompt)` and `get_valid_rate(prompt)`: Helper functions for input validation.
     - `format_currency(value)`: Formats numerical results as currency.
     - `main()`: Entry point that orchestrates the input, calculation, and output display.

2. **test_project.py** (Testing File)
   - **Tests**:
     - `test_calculate_compound_interest()`: Verifies compound interest calculations.
     - `test_calculate_future_value()`: Tests future value calculations.
     - `test_calculate_loan_payment()`: Checks the accuracy of loan repayment calculations.

## Design Principles
The design of the Compound Interest Calculator emphasizes simplicity, accuracy, and user-friendliness. It leverages modular programming and testing best practices to ensure reliable and consistent results. The use of NumPy for mathematical operations further enhances the accuracy of financial computations. The accompanying README.md provides a comprehensive guide to using the tool effectively.



