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


![Problem Statement](https://github.com/Atharavkag/Debt-settlement-calculator/blob/main/src/graph.png)

The graph shows the following transactions:

*   Pragy lends 500 to Murphy.
*   Pragy lends 320 to John.
*   Murphy lends 250 to John.
*   John lends 200 to Pragy.

In the application, you would enter these as follows:

*   Borrower: `Murphy`, Lender: `Pragy`, Amount: `500`
*   Borrower: `John`, Lender: `Pragy`, Amount: `320`
*   Borrower: `Murphy`, Lender: `John`, Amount: `250`
*   Borrower: `Pragy`, Lender: `John`, Amount: `200`

**Explanation of the Example and Simplification:**

The initial graph shows multiple debts between the three people. The goal of the debt settlement algorithm is to simplify these multiple debts into the fewest possible transactions to settle everyone up.

*   **Initial Debts:**
    *   Pragy is owed 200 by John.
    *   Pragy lent out a total of 500 + 320 = 820
    *   Murphy owes 500 to Pragy and is owed 250 by John, so Murphy's net debt is 500 - 250 = 250 owed to Pragy.
    *   John owes 320 to Pragy, so John's net debt is 120 + 250 = 370 owed to Pragy.

*   **Simplified Debts (as shown in the simplified graph):**
    *   Murphy owes 250 to Pragy.
    *   John owes 370 to Pragy.

The algorithm calculates these net balances and then determines the most efficient way to settle them. In this case, the simplified graph shows the optimal settlement: Murphy directly pays 250 to Pragy, and John directly pays 370 to Pragy. These two transactions settle all debts.

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
