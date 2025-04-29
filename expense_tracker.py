#Initialize CSV for Data Storage
import pandas as pd
import matplotlib.pyplot as plt

filename = 'expenses.csv'
try:
    data = pd.read_csv(filename)
except FileNotFoundError:
    column = ['Date', 'Category', 'Description', 'Amount']
    data = pd.DataFrame(columns=column)
    data.to_csv(filename, index=False)
#Function to add expenses    
def add_expense():
    date = input("Enter the date (YYYY-MM-DD): ")
    category = input("Enter the category (e.g., Food, Travel, Bills): ")
    description = input("Enter the description: ")
    amount = float(input("Enter the amount: ")) 

    new_entry = pd.DataFrame([{
        'Date': date, 
        'Category': category, 
        'Description': description, 
        'Amount': amount}])
    global data
    data = pd.concat([data, new_entry], ignore_index=True)
    data.to_csv(filename, index=False)
    print("Expense added successfully!")
#Function to view expenses
def view_expenses():
    print("\nYour Recorded Expenses:")
    print(data)

#Generating Analytics
def generate_report():
    if data.empty:
        print("No data available to analyze.")
        return
    #Group data by category
    summary = data.groupby('Category')['Amount'].sum()
    #Display Bar chart
    summary.plot(kind='bar', title='Expenses by Category', color='skyblue')
    plt.ylabel('Amount Spent')
    plt.show()
    #Display Pie chart
    summary.plot(kind='pie', autopct='%1.1f%%')
    plt.title('Expense Distribution')
    plt.ylabel('')
    plt.show()
#Main Menu to Navigate
while True:
    print("\nExpense Tracker Menu:")
    print("1. Add Expense")
    print("2. View Expense")
    print("3. Generate Analytics") 
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        add_expense()
    elif choice == '2':
        view_expenses()
    elif choice == '3':
        generate_report()
    elif choice == '4':
        print("Exiting... Have a great day ahead!")
        break
    else:
        print("Invalid choice. Please try again.")