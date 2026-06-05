budget = 0
expenses = []

def add_expense():
    expense = input('Amount (Toman): ')
    cat = input('Category: ')
    desc = input('Description: ')
    
    expense_item = {
        'amount': int(expense),
        'category': cat,
        'description': desc
    }
    expenses.append(expense_item)
    print('✅ Expense Added')
    #print('======')

def show_report():
    print('\n=== REPORT ===')
    print(expenses)
    
    if not expenses:
        print("No expenses yet.")
        return
    
    total = 0
    amounts = []
    for item in expenses:
        amt = item['amount']
        total += amt
        amounts.append(amt)
    
    max_amount = max(amounts)
    remaining = budget - total
    percent = (total / budget) * 100 if budget > 0 else 0
    
    print(f'Total spent: {total} Toman')
    print(f'Budget left: {remaining} Toman')
    print(f'Used: {percent:.1f}% of budget')
    print(f'Largest expense: {max_amount} Toman')
    
    if percent >= 80:
        print('⚠️ Warning! Only 20% of budget left!')
    if total >= budget:
        print('💀 Budget exhausted! Stop spending.')
    #print('======')

def top_categories():
    print('\n=== TOP CATEGORIES ===')
    if not expenses:
        print("No expenses yet.")
        return
    
    cat_totals = {}
    for item in expenses:
        cat = item['category']
        amt = item['amount']
        cat_totals[cat] = cat_totals.get(cat, 0) + amt
    
    sorted_cats = sorted(cat_totals.items(), key=lambda x: x[1], reverse=True)
    
    print("Most spending categories:")
    for i, (cat, amt) in enumerate(sorted_cats[:3], 1):
        print(f"{i}. {cat}: {amt} Toman")
    #print('======')

def main_menu():
    global budget
    budget = int(input('Enter your monthly budget (Toman): '))
    
    while True:
        print('\n--- Budget Track ---')
        print('1. Add Expense')
        print('2. Show Report')
        print('3. Top Categories')
        print('4. Exit')
        digit = input('Choose: ')
        
        if digit == '1':
            add_expense()
        elif digit == '2':
            show_report()
        elif digit == '3':
            top_categories()
        elif digit == '4':
            print('Thank you, Goodbye!')
            break
        else:
            print('ERROR! Choose 1, 2, 3 or 4')

main_menu()