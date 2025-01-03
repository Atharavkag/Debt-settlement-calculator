# Debt Settlement Calculator 💸

This Python application uses Tkinter to provide a graphical user interface for simplifying and optimizing debt settlements between multiple parties. It takes transaction data as input and calculates the net balances for each person, then determines the most efficient way to settle all debts with the fewest possible transactions.

## Features ✨

*   **User-friendly GUI:** Built with Tkinter for easy input and clear display of results. 🖥️
*   **Simple Transaction Input:** Input borrower, lender, and amount for each transaction. 📝
*   **Balance Calculation:** Computes the net balance (amount owed or owed to) for each participant. ⚖️
*   **Optimal Settlement Calculation:** Determines the minimum number of transactions needed to settle all debts. 🧮
*   **Clear Output:** Displays both the net balances and the optimal settlement transactions in a readable format. 📰
*   **Input Validation:** Includes error handling to prevent invalid inputs. ✅

## Input Format

The application expects input in the following format, entered through the GUI:

For each transaction:

*   **Borrower:** The name of the person who borrowed the money. 🙇
*   **Lender:** The name of the person who lent the money. 🏦
*   **Amount:** The amount of money borrowed (a positive number). 💰

You add transactions one by one using the "Add Transaction" button.

**Example Input:**

Let's say the following transactions occurred:

*   Alice lent $100 to Bob.
*   Alice lent $50 to Charlie.
*   Bob lent $20 to Charlie.

In the application, you would enter these as follows:

*   Borrower: `Bob`, Lender: `Alice`, Amount: `100`
*   Borrower: `Charlie`, Lender: `Alice`, Amount: `50`
*   Borrower: `Charlie`, Lender: `Bob`, Amount: `20`

## How to Run 🚀

1.  Make sure you have Python 3 installed. 🐍
2.  Save the Python code (e.g., `debt_settlement_gui.py`). 💾
3.  Run the script from your terminal: `python debt_settlement_gui.py` 💻

## Code Structure 🏗️

The code is organized into the following functions:

*   `org(transactions)`: Calculates the net balance for each person. 📊
*   `portion(balances)`: Determines the optimal settlements. 🎯
*   `transaction()`: Handles the input of individual transactions. ➕
*   `calculate()`: Parses input from the GUI, calls the calculation functions, and displays the results. ⚙️

## Dependencies 📦

*   `tkinter`: For the graphical user interface (standard library).

This README provides a comprehensive overview of the application, its features, usage, and code structure. It should help users understand and use the debt settlement calculator effectively. 👍
