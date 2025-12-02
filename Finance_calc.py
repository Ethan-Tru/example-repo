# Let the user choose investment or home loan repayment
print("Investment- to calculate the amount of interest you will earn")
print("Bond- to calculate the amount you will have to pay on a home loan")
print(" ")
# Make investment, bond, simple and compund interest as variables
invest = "Investment"
bond = "Bond"
simple = "Simple"
compound = "Compound"
# Convert all answers to uppercase
ask = input(f"Enter either {invest} or {bond} from the menu above to continue: ").upper()
print(" ")
if ask == invest.upper(): # if ask is = to invest then it will ask these questions
    money = int(input("Please enter the amount of money you are depositing: "))
    rate = int(input("Please enter the interest rate as a percentage. Only the number should be entered: "))
    years = int(input("Please enter the number of years you plan on investing for: "))
    interest = input(f"Please enter either {simple} or {compound}: ").upper()
    if interest == simple.upper(): # if interest is = to simple then this equation will be used
        r = rate/100
        answer1 = money * (1 + r * years)
        print(" ")
        print(f"The amount you will earn with simple interest will be: {answer1} ")
    elif interest == compound.upper(): # if interest is = to compound then this equation will be used
        import math
        r = rate/100
        answer2 = money * math.pow((1 + r),years)
        print(" ")
        print(f"The amount you will earn with compound interest will be: {answer2}")
elif ask == bond.upper(): # if ask = to bond then these questions and equatio will be used
    value = int(input("Please enter the present value of the house: "))
    bond_rate = int(input("Please enter the interest rate as a percentage. Only the number should be enetered: "))
    months = int(input("Please enter the number of months you plan to take to repay the bond: "))
    br = bond_rate/100
    monthly_interest_rate = br / 12
    monthlypay = (value * monthly_interest_rate) / (1 - (1 + monthly_interest_rate) ** - months) 
    print(" ")
    print(f"The monthly repayment will be: {monthlypay} ")
else: # Error message if something else is typed
    error = ("ERROR. You did not enter 'Investment' or 'Bond'. ")
    print(f"{error}")