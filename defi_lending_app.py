from tkinter import *

# -----------------------------
# Mock DeFi Contract (Simulation)
# -----------------------------
class DeFiContract:
    def __init__(self):
        # Dictionary to store user balances
        self.balances = {}

    def deposit(self, user, amount):
        # Add amount to user's balance
        if user in self.balances:
            self.balances[user] += amount
        else:
            self.balances[user] = amount

    def withdraw(self, user, amount):
        # Check if user has enough balance
        if user in self.balances and self.balances[user] >= amount:
            self.balances[user] -= amount
            return True
        return False

    def get_balance(self, user):
        return self.balances.get(user, 0)


# Create contract instance
contract = DeFiContract()

# -----------------------------
# GUI Functions
# -----------------------------
def deposit():
    user = entry_user.get()
    amount = float(entry_amount.get())

    contract.deposit(user, amount)
    result.set(f"Deposited {amount} ETH for {user}")

def withdraw():
    user = entry_user.get()
    amount = float(entry_amount.get())

    if contract.withdraw(user, amount):
        result.set(f"Withdrawn {amount} ETH for {user}")
    else:
        result.set("Insufficient Balance!")

def check_balance():
    user = entry_user.get()
    balance = contract.get_balance(user)
    result.set(f"Balance of {user}: {balance} ETH")


# -----------------------------
# Tkinter UI
# -----------------------------
root = Tk()
root.title("DeFi Lending Simulation")

Label(root, text="User Name").grid(row=0, column=0)
Label(root, text="Amount (ETH)").grid(row=1, column=0)

entry_user = Entry(root)
entry_amount = Entry(root)

entry_user.grid(row=0, column=1)
entry_amount.grid(row=1, column=1)

Button(root, text="Deposit", command=deposit).grid(row=2, column=0)
Button(root, text="Withdraw", command=withdraw).grid(row=2, column=1)
Button(root, text="Check Balance", command=check_balance).grid(row=3, column=0, columnspan=2)

result = StringVar()
Label(root, textvariable=result, fg="blue").grid(row=4, column=0, columnspan=2)

root.mainloop()