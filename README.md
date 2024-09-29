 # Compound Interst Calculator

    #### Video Demo:  https://youtu.be/WpeMyAof-xw

    #### Description:

    The Compound Interest Calculator is a Python-based financial tool designed to help users perform essential financial calculations. This project focuses on providing users with an intuitive way to calculate compound interest, determine the future value of regular investments, and compute the monthly payments required to repay a loan. The calculator ensures that users can make informed financial decisions by offering accurate and easy-to-understand results.

    Files and Their Contents
    1. project.py
    This is the main file of the project, containing the core functionalities:

    calculate_compound_interest(principal, rate, years): This function calculates the total amount accumulated after a specified number of years, considering compound interest. It takes the initial principal, the annual interest rate, and the number of years as inputs. The result is formatted as a currency string.

    calculate_future_value(payment, rate, periods): This function calculates the future value of a series of regular payments (e.g., monthly investments) over a specified period. It uses the interest rate per period and the total number of periods to determine the final value of the investments.

    calculate_loan_payment(principal, rate, periods): This function determines the fixed monthly payment required to repay a loan. It considers the loan amount (principal), the monthly interest rate, and the total number of payments.

    get_valid_amount(prompt) and get_valid_rate(prompt): These helper functions ensure that the user inputs are valid. They prompt the user until a positive numerical value is provided. The get_valid_rate function also converts the annual interest rate from a percentage to a decimal for accurate calculations.

    format_currency(value): This function formats numerical results as currency, ensuring all outputs are displayed with two decimal places and a dollar sign, making them clear and user-friendly.

    main(): The entry point of the program, which orchestrates the entire process. It prompts the user for input values, invokes the relevant calculation functions, and prints the results in a clear and concise manner.

    2. test_project.py
    This file contains the test cases for the core functions in project.py:

    test_calculate_compound_interest(): Tests the accuracy of the compound interest calculations against known values.
    test_calculate_future_value(): Verifies that the future value calculations for regular payments are correct.
    test_calculate_loan_payment(): Ensures that the loan payment calculations return the correct monthly payment.


    The design of the Compound Interest Calculator was guided by the principles of simplicity, accuracy, and user-friendliness.Another design decision was to use numpy for handling mathematical operations, particularly exponentiation, to ensure accuracy and consistency in the calculations.

    This project not only demonstrates the core concepts of financial calculations but also showcases best practices in Python programming, including modularity, testing, and user-friendly design. The accompanying README.md provides a comprehensive overview of the project, ensuring that users and developers alike can understand and utilize the tool effectively.



