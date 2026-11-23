import json

class ExpenseTracker:
    def __init__(self, user):
        self.user = user
        self.expense_model = []
        self.load_expenses()

    def add_expense(self):
        amount = int(input('How much do you want to add?$ '))
        while amount <= 0:
                print('You enterd an amount less than 0')
                amount = int(input('How much do you want to add?$ '))
        print('Category includes food, transportation, health, stipend, accommodation, clothing etc')
        category = input('What category is your money meant for? ').strip().title()
        description = input('Describe your expense category: ').strip().capitalize()

        expenses = {
                'amount':amount,
                'category':category,
                'description':description
        }
            
        self.expense_model.append(expenses)
        self.save_expense()

        print('Expense added successfully')

    def save_expense(self):
        try:
            with open('expense_tracker.json', 'r') as file:
                expense_model = json.load(file)
        except FileNotFoundError:
            expense_model = {}

        expense_model[self.user] = self.expense_model

        with open('expense_tracker.json', 'w') as file:
            json.dump(expense_model, file, indent=4)

    def load_expenses(self):
        try:
            with open('expense_tracker.json', 'r') as file:
                expense_model = json.load(file)

            if self.user in expense_model:
                self.expense_model = expense_model[self.user]
            else:
                self.expense_model = []

        except FileNotFoundError:
            self.expense_model = []

    def view_expense(self):
        if not self.expense_model:
            print('No expenses found.')
            return

        print(f'\nExpenses for {self.user}:')

        for payment in self.expense_model:
            print(
                f"Amount: ${payment['amount']} | "
                f"Category: {payment['category']} | "
                f"Description: {payment['description']}"
            )

    def calculate_expense(self):
        if not self.expense_model:
            print('There are no expenses saved yet.')
            return

        total = sum(payment['amount'] for payment in self.expense_model)

        print(f'\nTotal expenses for {self.user}: ${total}')

        user1 = input('Do you want to calculate by category? Type yes or  no: ').lower()
        if user1 == 'yes':

            spending = {}

            for payment in self.expense_model:
                if payment['category'] in spending:
                    spending[payment['category']] += payment['amount']
                else:
                    spending[payment['category']] = payment['amount']

            print('\nExpenses by category:')

            for category, amount in spending.items():
                print(f'{category}: ${amount}')

        elif user1 == 'no':
            print('Thank you, that will be all for now.')
        else:
            print("You didn't type the right option.")

    def delete_expense(self):
        if not self.expense_model:
            print('There are no expenses to delete.')
            return

        print('\nYour expenses:')

        for index, payment in enumerate(self.expense_model, start=1):
            print(
                f"{index}. "
                f"Amount: ${payment['amount']} | "
                f"Category: {payment['category']} | "
                f"Description: {payment['description']}"
            )

        try:
            delete = int(input('\nEnter the number of the expense you want to delete: '))

            if delete < 1 or delete > len(self.expense_model):
                print('You typed an invalid expense number.')
                return

            deleted_expense = self.expense_model.pop(delete - 1)

            self.save_expense()

            print(
                f"Expense deleted successfully: "
                f"${deleted_expense['amount']} - "
                f"{deleted_expense['description']}"
            )

        except ValueError:
            print('Wrong request!')

def get_user(expense_model):
    print("Hey, let's get you registerd or signed-in!")
    try:
        firstname = input('Enter your firstname: ').strip().title()
        lastname = input('Enter your lastname: ').strip().title()
        user = firstname + " " + lastname
        if user not in expense_model:
                expense_model[user] = []

                with open('expense_tracker.json', 'w') as file:
                    json.dump(expense_model, file, indent=4)

                print(f'Welcome, {user}! Your account has been created.')
        else:
            print(f'Welcome back, {user}!')
            return user
    except ValueError:
            print('Please type a correct user name.')

try:
    with open('expense_tracker.json', 'r') as file:
        expense_model = json.load(file)

except FileNotFoundError:
    expense_model = {}


user = get_user(expense_model)

tracker = ExpenseTracker(user)

while True:
    print(f'Logged in as: {user}')   
    print('-'*30)
    print('EXPENSE TRACKER'.center(30))
    print('-'*30)
    print('List of things you could do today.')
    print('1. Choose 1 to Add_Expense')
    print('2. Choose 2 to View_Expense')
    print('3. Choose 3 to Calculate_Expense')
    print('4. Choose 4 to Delete_Expense')
    print('5. Choose 5 to Exit')

    try:
        ask_user = int(input('What are you doing today? \n'))
        if ask_user == 1:
            tracker.add_expense()

        elif ask_user == 2:
            tracker.view_expense()

        elif ask_user == 3:
            tracker.calculate_expense()

        elif ask_user == 4:
            tracker.delete_expense()

        elif ask_user == 5:
            print('Thank you. See you later!')
            break

        else:
            print('You typed a wrong option.')

    except ValueError:
        print('Wrong request!')


