class Home:
    
    def __init__(self):
        self.income = {}
        self.expenses = {}
        self.cash_flow = {}
        self.ROI = {}
        self.income_total = 0
        self.expenses_total = 0
        self.cash_flow_total = 0
        self.total_investment = 0

    def income_calc(self):
        rental_income = int(input("What is your monthly rental income? "))
        self.income['Rental Income'] = rental_income
        laundry_income = int(input("What is your monthly laundry income? "))
        self.income['Laundry Income'] = laundry_income
        storage_income = int(input("What is your monthly storage income? "))
        self.income['Storage Income'] = storage_income
        misc_income = int(input("Please input any remaining miscellaneous property income: "))
        self.income['Misc Income'] = misc_income

        income_total = sum(self.income.values())
        self.income_total = income_total
        print(f"Your monthly income is: {income_total}")

    def expenses_calc(self):
        print("Now let's calculate your monthly expenses.")

        tax_expense = int(input("What is your monthly tax expense? "))
        self.expenses['Tax Expense'] = tax_expense
        insurance_expense = int(input("What is your monthly insurance expense? "))
        self.expenses['Insurance Expense'] = insurance_expense
        utilities_expense = int(input("What is your monthly utilities expense? "))
        self.expenses['Utilities Expense'] = utilities_expense
        HOA_expense = int(input("What is your monthly home owners association expense? "))
        self.expenses['HOA Expense'] = HOA_expense
        lawn_expenses = int(input("What is your monthly lawn and snow expenses? "))
        self.expenses['Lawn and Snow Expense'] = lawn_expenses
        vacancy_expenses = int(input("What is your monthly vacancy expenses? "))
        self.expenses['Vacancy Expense'] = vacancy_expenses
        repairs_expense = int(input("What is your monthly repairs expense? "))
        self.expenses['Repairs Expense'] = repairs_expense
        capex_expense = int(input("What is your monthly expense for big fixes? "))
        self.expenses['Cap Ex Expense'] = capex_expense
        propertymanagement_expense = int(input("What is your monthly property management expense? "))
        self.expenses['Property Management Expense'] = propertymanagement_expense
        mortgage_expense = int(input("What is your monthly mortgage expense? "))
        self.expenses['Mortgage Expense'] = mortgage_expense

        expense_total = sum(self.expenses.values())
        self.expenses_total = expense_total
        print(f"Your monthly expenses are: {expense_total}")

    
    def cash_flow_calc(self):
        cash_flow = self.income_total - self.expenses_total
        self.cash_flow_total = cash_flow
        annual_cash_flow = self.cash_flow_total * 12
        self.annual_cash_flow = annual_cash_flow
        print(f"Thanks for the information so far. Your monthly cash flow is: {cash_flow}. Annyally that comes out to be: {annual_cash_flow}")


    def ROI_calc(self):
        print("Now let's calculate your cash on cash ROI.")
        down_payment = int(input("What was your down payment? "))
        self.ROI['Down Payment'] = down_payment
        closing_costs = int(input("How much did you spend on your closing costs? "))
        self.ROI['Closing Costs'] = closing_costs
        rehab_budget = int(input("How much did you spend on renovations? "))
        self.ROI['Renovations'] = rehab_budget
        miscellaneous = int(input("How much have you spent on miscellaneous reasons? "))
        self.ROI['Miscellaneous'] = miscellaneous

        total_investment = sum(self.ROI.values())
        self.total_investment = total_investment
        
        ROI = self.annual_cash_flow / total_investment * 100
        print(f"Your Cash on Cash ROI is: {ROI}%")


    def edit_entry(self, dictionary, key, value):
        


def run():
    my_home = Home()
    while True:
        opening = input('Welcome to the ROI Home Calculator. Would you like to check the ROI on your home investment? ')
        if opening.title() == "Yes":
            my_home.income_calc()
            my_home.expenses_calc()
            my_home.cash_flow_calc()
            my_home.ROI_calc()
            # give options to edit, view, or quit
        elif opening.title() == "No":
            print("Sure, now problem. Please come back when you are ready!")
            break
        else:
            print("That is an invalid option. Please enter 'Yes' or 'No'.")
run()