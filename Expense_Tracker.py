import json

amount = 0
def add_expense():
    global amount
    # user = input('Enter your name: ').strip().title()
    amount = int(input('How much do you want to add?$ '))
    while amount <= 0:
            print('You enterd an amount less than 0')
            amount = int(input('How much do you want to add?$ '))
    print('Category includes food, transportation, health, stipend, accommodation, clothing etc')
    category = input('What category is your money meant for? ').strip().title()
    description = input('Describe your expense category: ').strip().capitalize()

    expense_model = {
            # 'user':user,
            'amount':amount,
            'category':category,
            'description':description
    }
        
    return expense_model

def save_expense(expense_model, expenses):
    expense_model.append(expenses)
    with open('expense_tracker.json', 'w') as file:
        json.dump(expense_model, file, indent=4)

def view_expense():
    try:
        with open('expense_tracker.json', 'r') as file:
            expense_model = json.load(file)
            # print(expense_model)

            if isinstance(expense_model, dict):
                expense_model = [expense_model]
            return expense_model
    except FileNotFoundError:
        return []

def calculate_expense(expense_model):
    # expense_model = view_expense()

    if not expense_model:
        print('There are no expenses saved yet.')
        return

    total = sum(payment['amount'] for payment in expense_model) #this is  lambda function

    print(f'\nYour total expenses for everyone: ${total}')

    user1 = input('Do you want to calculate by category? ').lower()
    if user1 == 'yes':
        spending = {}
        for payment in expense_model:
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
        print("You didn't type the right option")

def delete_expense(expense_model):
    # expense_model = view_expense()

    if not expense_model:
        print('There are no expenses to delete.')
        return

    print('\nWhat do you want to delete?')
    print('1. Category')
    print('2. Amount')
    print('3. Description')

    try:
        delete = int(input('Choose an option: '))

        if delete == 1:
            category = input('Enter the category to delete: ').strip().title()

            expense_model = [
                payment for payment in expense_model
                if payment['category'] != category
            ]

        elif delete == 2:
            amount = int(input('Enter the amount to delete: '))

            expense_model = [
                payment for payment in expense_model
                if payment['amount'] != amount
            ]

        elif delete == 3:
            description = input('Enter the description to delete: ').strip().capitalize()

            expense_model = [
                payment for payment in expense_model
                if payment['description'] != description
            ]

        else:
            print('You typed a wrong option.')
            return

        with open('expense_tracker.json', 'w') as file:
            json.dump(expense_model, file, indent=4)

        print('Expense deleted successfully.')

    except ValueError:
        print('Wrong request!')

expense_model = view_expense()

while True:   
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
        ask_user = int(input('What are you doing today? '))
        if ask_user == 1:
            expenses = add_expense()
            save_expense(expense_model, expenses)
            # expense_model = view_expense()
            print('Expense added successfully.')
        elif ask_user == 2:
            # expense_model = view_expense()

            if not expense_model:
                print('No expenses found.')

            else:
                print('\nSaved expenses:')

                for payment in expense_model:
                    print(
                        # f"User: {payment['user']} | "
                        f"Amount: ${payment['amount']} | "
                        f"Category: {payment['category']} | "
                        f"Description: {payment['description']}"
                    )
        elif ask_user == 3:
            calculate_expense(expense_model)
        elif ask_user == 4:
            delete_expense(expense_model)
            expense_model = view_expense()
        elif ask_user == 5:
            print('Thank you. See you later!')
            break
        else:
            print('You typed a wrong option.')
    except ValueError:
        print('Wrong request!')










































































































