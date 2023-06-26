import math

print("Select an option: \n1.Investment \n2.Bond")

invest_or_bond = input(str("Enter option: \n")).lower()

if invest_or_bond == "investment":
    if True:
        p = float(input("Enter the amount you are depositing:\n"))
        r = float(input("Enter the interst rate:\n"))
        r = (r/100) /12
        t = float(input("Enter the duration of years you plan to investment:\n"))
        simp_comp = str(input("Choose from 'Simple' or 'Compound' interest. \n")).lower()

        if simp_comp == "Simple":
            "Simple" == simp_comp
            simp_comp = p*(1 + r * t)
            total = simp_comp
            print (f"The interst you have earned over {t} years will be: {total:.2f}".format())
        elif simp_comp:
            simp_comp = p*math.pow((1+r),t)
            total = simp_comp
            print (f"The interest you have earned over {t} years will be: {total:.2f}".format())

elif invest_or_bond == "bond":
    if True:
        p = float(input("What is the current value of the property?\n"))
        i = float(input("Enter the interest rate in percentage:\n"))
        i = ((i/100)/12) /12
        n = float(input("Enter the duration of months you plan to repay:\n"))
        Monthly_repay = float(math.floor((i*p)/(1 - (1+i)**(-n))))
        print(f"Monthly repayment: {Monthly_repay:.2f}".format())
else:
    print("Error: Invalid input. Please try again.")