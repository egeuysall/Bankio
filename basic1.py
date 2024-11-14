class Account:
    def __init__(self):
        self.selectName = ""
        self.accountBalance = 0

    def createAccount(self):
        while True:
            try:
                self.selectName = input("Enter your name: ")
                # Checking if input is a number (to avoid it being invalid)
                float(self.selectName)  
                print("Please don't enter a number!")  # This message is triggered for a name being a number
            except ValueError:
                print(f"Welcome to Bankio, {self.selectName}!")
                break  # Breaks out of the loop once a valid name is entered

class Actions:
    def __init__(self, account):
        self.account = account  # Links Actions to the Account instance

    def depositMoney(self):
        while True:
            try:
                depositAmount = int(input("Enter the amount you want to deposit: "))
                # Add the deposit amount to the current account balance
                self.account.accountBalance += depositAmount
                print(f"${depositAmount} transferred to your account successfully!")
                break  # Exit loop after successful deposit
            except ValueError:
                print("Please enter a valid number!")

    def withdrawMoney(self):
        while True:
            try:
                withdrawAmount = int(input("Enter the amount you would like to withdraw: "))
                # Check if withdrawal amount exceeds balance
                if withdrawAmount > self.account.accountBalance:
                    print(f"You don't have ${withdrawAmount}, please enter a smaller value!")
                else:
                    # Subtract the withdrawal amount from the account balance
                    self.account.accountBalance -= withdrawAmount
                    print(f"You withdrew ${withdrawAmount} successfully!")
                    break  # Exit loop after successful withdrawal
            except ValueError:
                print("Please enter a valid number!")

    def checkBalance(self):
        # Print the current account balance
        print(f"Your account balance is ${self.account.accountBalance}")


class Program:
    def __init__(self):
        self.account = Account()  # Create an instance of Account
        self.actions = Actions(self.account)  # Pass the Account instance to Actions

    def main(self):
        print("Let's create your account!")
        self.account.createAccount()  # Call the createAccount method on the Account instance

        # Menu loop to handle different user actions
        while True:
            try:
                action = int(input("What would you like to do next?\n1. Deposit\n2. Withdraw\n3. Check Balance\n"))
                if action == 1:
                    self.actions.depositMoney()  # Call depositMoney from Actions
                elif action == 2:
                    self.actions.withdrawMoney()  # Call withdrawMoney from Actions
                elif action == 3:
                    self.actions.checkBalance()  # Call checkBalance from Actions
                else:
                    print("Please enter either 1, 2, or 3!")  # Invalid choice handling

                continue_action = input("Do you want to perform another action? (y/n): ").lower()
                if continue_action != 'y':
                    break  # Exit the loop if user does not want to continue

            except ValueError:
                print("Please enter a valid number!")

        print(f"Thanks for using Bankio, {self.account.selectName}! Your final balance is ${self.account.accountBalance}")


if __name__ == "__main__":
    program = Program()  # Create an instance of Program
    program.main()  # Run the main method of Program
