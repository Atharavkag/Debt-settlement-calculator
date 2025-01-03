import tkinter as tk
from tkinter import ttk, messagebox

def org(transistionlist):
    status = {}
    for bnam, indic in transistionlist.items():
        if bnam not in status:
            status[bnam] = 0
        for lnam, paisa in indic.items():
            if lnam not in status:
                status[lnam] = 0
            status[bnam] -= paisa
            status[lnam] += paisa
    return status


def portion(status):
    positive = []
    negative = []
    for nam, balance in status.items():
        if balance > 0:
            positive.append((nam, balance))
        elif balance < 0:
            negative.append((nam, balance))
    trans = []
    while positive and negative:
        lnam, lbalance = positive[0]
        bnam, bbalance = negative[0]
        trans_amount = min(lbalance, -bbalance)
        trans.append((bnam, lnam, trans_amount))
        positive[0] = (lnam, lbalance - trans_amount)
        negative[0] = (bnam, bbalance + trans_amount)
        if positive[0][1] == 0:
            positive.pop(0)
        if negative[0][1] == 0:
            negative.pop(0)
    return trans


def transaction():
    global trans
    bnam = bentry.get()
    lnam = lentry.get()
    amount = aentry.get()
    try:
        amount = int(amount)
    except ValueError:
        messagebox.showerror("Input Error!!!", "Please enter valid borrower, lender, and amount.")
        return

    if not bnam or not lnam:
        messagebox.showerror("Input Error!!!", "Borrower and Lender fields cannot be empty.")
        return

    if bnam not in trans:
        trans[bnam] = {}
    if lnam in trans[bnam]:
        trans[bnam][lnam] += amount
    else:
        trans[bnam][lnam] = amount
    tlist.insert(tk.END, f"{bnam} owes {lnam} ₹{amount}")
    bentry.delete(0, tk.END)
    lentry.delete(0, tk.END)
    aentry.delete(0, tk.END)


def calculate():
    global trans
    balance = org(trans)
    settle = portion(balance)

    result.set("Whole Story:\n")
    for nam, bal in balance.items():
        if bal > 0:
            result.set(result.get() + f"{nam} is owed ₹{bal}\n")
        elif bal < 0:
            result.set(result.get() + f"{nam} owes ₹{abs(bal)}\n")
        else:
            result.set(result.get() + f"{nam} is settled.\n")
    
    result.set(result.get() + "\nOptimal Settlements:\n")
    if settle:
        for bnam, lnam, amount in settle:
            result.set(result.get() + f"{bnam} pays {lnam} ₹{amount}\n")
    else:
        result.set(result.get() + "Everyone is settled up!!")


trans = {}
root = tk.Tk()
root.title("Cash Flow Minimizer")

tk.Label(root, text="Borrower:").grid(row=0, column=0, padx=5, pady=5)
bentry = tk.Entry(root)
bentry.grid(row=0, column=1)

tk.Label(root, text="Lender:").grid(row=1, column=0, padx=5, pady=5)
lentry = tk.Entry(root)
lentry.grid(row=1, column=1)

tk.Label(root, text="Amount:").grid(row=2, column=0, padx=5, pady=5)
aentry = tk.Entry(root)
aentry.grid(row=2, column=1)

tk.Button(root, text="Add Transaction", fg="white", bg="black", font=("arial", 13), command=transaction).grid(row=3, column=0, pady=10)
tk.Button(root, text="Calculate Settlements", fg="white", bg="black", font=("arial", 13), command=calculate).grid(row=3, column=1)

tk.Label(root, text="Transactions:", font=("arial", 13)).grid(row=4, column=0, columnspan=2)
tlist = tk.Listbox(root, width=60, height=10)
tlist.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

result = tk.StringVar()
result_label = tk.Label(root, textvariable=result, justify="left", anchor="w", font=("arial", 10))
result_label.grid(row=6, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()

'''5
A 2 t1 t2
B 1 t1
C 1 t1
D 1 t2
E 1 t2
4
B A 300
C A 700
D B 500
E B 500

--------

5
A 2 t1 t2
B 1 t1
C 1 t1
D 1 t2
E 1 t2
4
B A 300
C A 700
D B 500
E B 500

--------------------

6
B 3 1 2 3
C 2 1 2
D 1 2
E 2 1 3
F 1 3
G 2 2 3
9
G B 30
G D 10
F B 10
F C 30
F D 10
F E 10
B C 40
C D 20
D E 50'''


