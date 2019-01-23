def accounting_equation():
    
    owners_enquity = int (input ("enter owners_enquity :"))
    rent = int (input ("enter your rent:"))
    product_cost = int (input ("enter your product cost:"))
    current_bill =  int (input ("enter your current bill:"))
    ppl_working =  int (input ("enter number of people working:"))
    salary = int (input ("enter salary :"))
    tot_salary = ppl_working  * salary
    liability = rent + product_cost + current_bill + tot_salary
    assest = liability + owners_enquity
    print (assest)
    
    
def net_income():
    revenue = int (input ("enter your revenue :"))
    expenses = int (input ("enter your expenses :"))
    net_income = revenue - expenses
    print ("net_income",net_income)
    return(net_income)


def break_even_point():
    fixed_price = int(input ("enter your fixed price :"))
    sales_price = int(input ("enter your sales price :"))
    amount = int (input ("enter amount for making products:"))
    break_even_point = fixed_price / sales_price - amount
    print ("break_even point :", break_even_point)

def cash_ratio():
    cash =  int (input ("enter cash :"))
    rent = int (input ("enter your rent:"))
    produt_cost = int (input ("enter your product cost:"))
    current_bill =  int (input ("enter your current bill:"))
    ppl_working =  int (input ("enter number of people working:"))
    salary = int (input ("enter salary :"))
    tot_salary = ppl_working  * salary
    liability = rent + product_cost + current_bill + tot_salary
    cash_ratio = cash / liability
    print ("cash ratio",cash_ratio)
    
def profit_margin():
    sales = int(input("enter your sales:"))
    income = net_income()
    profit_margin = income /sales
    print ("profit margin", profit_margin)
    
def debt_to_equity_ratio():
    rent = int (input ("enter your rent:"))
    produt_cost = int (input ("enter your product cost:"))
    current_bill =  int (input ("enter your current bill:"))
    ppl_working =  int (input ("enter number of people working:"))
    salary = int (input ("enter salary :"))
    tot_salary = ppl_working  * salary
    liability = rent + product_cost + current_bill + tot_salary
    belongings = int (input ("hoe much companies belongs to you:"))
    debt_to_equity_ratio = liability / belongings
    print ("debt to equity ratio:",debt_to_equity_ratio )

def cost_of_sold_goods():
    materials_cost = int(input("enter the cost of materials:"))
    selling_price = int (input ("enter the selling price :"))
    cost_of_sold_goods =  materials_cost / selling_price
    print ("cost of sold goods :", cost_of_sold_goods)
    
choice=int(input("enter your choice:"))
if (choice==1):
    accounting_equation()
elif (choice == 2):
    net_income()
elif (choice == 3):
    break_even_point()
elif (choice == 4):
    cash_ratio()
elif (choice == 5):
    profit_margin()
elif (choice == 6):
    debt_to_equity_ratio()
else:
    cost_of_sold_goods()
    
print ("thank you")
    