# Debt Settlement Calculator

This Python application uses Tkinter to provide a graphical user interface for simplifying and optimizing debt settlements between multiple parties. It takes transaction data as input and calculates the net balances for each person, then determines the most efficient way to settle all debts with the fewest possible transactions.

## Features

*   **User-friendly GUI:** Built with Tkinter for easy input and clear display of results.
*   **Flexible Input Format:** Accepts transaction data in a structured format, allowing for multiple lenders per borrower.
*   **Balance Calculation:** Computes the net balance (amount owed or owed to) for each participant.
*   **Optimal Settlement Calculation:** Determines the minimum number of transactions needed to settle all debts.
*   **Clear Output:** Displays both the net balances and the optimal settlement transactions in a readable format.
*   **Input Validation:** Includes error handling to prevent invalid inputs.

## Input Format

The application expects input in the following format, entered through the GUI:

1.  **People and Affiliations:**
    *   The first input field asks for the number of people involved (`n`).
    *   Then, for each person:
        *   An input field prompts for the person's name.
        *   An input field prompts for the number of affiliations for that person.
        *   Based on the number of affiliations, input fields are dynamically created to enter the affiliation names. (Affiliations are currently read but not used in the core logic.)

2.  **Transactions:**
    *   After entering all people and their affiliations, you will be prompted to enter transactions.
    *   For each transaction:
        *   An input field for the borrower's name.
        *   An input field for the lender's name.
        *   An input field for the amount.

**Example Input (corresponding to the provided examples):**

**Example 1:**

*   Number of People: `5`
*   Person 1 Name: `A`
*   Person 1 Number of Affiliations: `2`
*   Person 1 Affiliation 1: `t1`
*   Person 1 Affiliation 2: `t2`
*   (Similarly for B, C, D, and E)
*   Number of Transactions: `4`
*   Transaction 1: Borrower: `B`, Lender: `A`, Amount: `300`
*   (Similarly for the other 3 transactions)

**Example 2:**

*   Number of People: `5`
*   Person 1 Name: `World_Bank`
*   Person 1 Number of Affiliations: `2`
*   Person 1 Affiliation 1: `Google_Pay`
*   Person 1 Affiliation 2: `PayTM`
*   (Similarly for Bank_B, Bank_C, Bank_D, and Bank_E)
*   Number of Transactions: `4`
*   Transaction 1: Borrower: `Bank_B`, Lender: `World_Bank`, Amount: `300`
*   (Similarly for the other 3 transactions)

**Example 3:**

*   Number of People: `6`
*   (Follow the same pattern as above)

## How to Run

1.  Make sure you have Python 3 installed.
2.  Save the Python code (e.g., `debt_settlement_gui.py`).
3.  Run the script from your terminal: `python debt_settlement_gui.py`

## Code Structure

The code is organized into the following functions:

*   `org(transactions)`: Calculates the net balance for each person.
*   `portion(balances)`: Determines the optimal settlements.
*   `calculate_and_display()`: Parses input from the GUI, calls the calculation functions, and displays the results.
*   `create_input_fields()`: Dynamically creates the input fields in the GUI based on the number of people.

## Dependencies

*   `tkinter`: For the graphical user interface (standard library).

## Further Improvements

*   **Affiliation Logic:** Implement the use of affiliations in the settlement calculations.
*   **Input Validation:** Add more robust validation to prevent non-numeric input for amounts and handle other potential input errors.
*   **Data Persistence:** Implement saving and loading of transaction data to/from a file.
*   **Improved GUI:** Enhance the GUI with better layout, styling, and user feedback.

This README provides a comprehensive overview of the application, its features, usage, and code structure. It should help users understand and use the debt settlement calculator effectively.
