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
        rental_income = input(int("What is your monthly rental income?"))
        self.income['Rental Income'] = rental_income
        laundry_income = input(int("What is your monthly laundry income?"))
        self.income['Laundry Income'] = laundry_income
        storage_income = input(int("What is your monthly storage income?"))
        self.income['Storage Income'] = storage_income
        misc_income = input(int("Please input any remaining miscellaneous property income: "))
        self.income['Misc Income'] = misc_income

        print(f"Your monthly income is: {self.income}")
        income_total = sum(self.income.values())
        self.income_total = income_total
        return income_total

    def expenses_calc(self):
        print("Now let's calculate your monthly expenses.")

        tax_expense = input(int("What is your monthly tax expense?"))
        self.expenses['Tax Expense'] = tax_expense
        insurance_expense = input(int("What is your monthly insurance expense?"))
        self.expenses['Tax Expense'] = tax_expense
        utilities_expense = input(int("What is your monthly utilities expense?"))
        self.expenses['Utilities Expense'] = utilities_expense
        HOA_expense = input(int("What is your monthly home owners association expense?"))
        self.expenses['HOA Expense'] = HOA_expense
        lawn_expenses = input(int("What is your monthly lawn and snow expenses?"))
        self.expenses['Lawn and Snow Expense'] = lawn_expenses
        vacancy_expenses = input(int("What is your monthly vacancy expenses?"))
        self.expenses['Vacancy Expense'] = vacancy_expenses
        repairs_expense = input(int("What is your monthly repairs expense?"))
        self.expenses['Repairs Expense'] = repairs_expense
        capex_expense = input(int("What is your monthly expense for big fixes?"))
        self.expenses['Cap Ex Expense'] = capex_expense
        propertymanagement_expense = input(int("What is your monthly property management expense?"))
        self.expenses['Property Management Expense'] = propertymanagement_expense
        mortgage_expense = input(int("What is your monthly mortgage expense?"))
        self.expenses['Mortgage Expense'] = mortgage_expense

        print(f"Your monthly expenses are: {self.expenses}")
        expense_total = sum(self.expenses.values())
        self.expenses_total = expense_total
        return expense_total
    
    def cash_flow_calc(self):
        cash_flow = self.income_total - self.expenses_total
        self.cash_flow_total = cash_flow
        print(f"Thanks for the information so far. Your cash flow is: {cash_flow}")
        return cash_flow

    def ROI_calc(self):
        print("Now let's calculate your cash on cash ROI.")
        down_payment = input(int("What was your down payment?"))
        self.ROI['Down Payment'] = down_payment
        closing_costs = input(int("How much did you spend on your closing costs?"))
        self.ROI['Closing Costs'] = closing_costs
        rehab_budget = input(int("How much did you spend on renovations?"))
        self.ROI['Renovations'] = rehab_budget
        miscellaneous = input(int("How much have you spent on miscellaneous reasons?"))
        self.ROI['Miscellaneous'] = miscellaneous
        total_investment = sum(self.ROI.values())
        self.total_investment = total_investment
        return total_investment






def run():
    opening = input('Welcome to the ROI Home Calculator. Would you like to check the ROI on your home investment? ')
    my_home = Home()
    while opening.lower == "yes" or "yes" in opening.lower:
        pass
        my_home.income_calc()
        my_home.expenses_calc()
        my_home.cash_flow_calc()
        my_home.ROI_calc()