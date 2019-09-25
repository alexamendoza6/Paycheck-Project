#inputs that  that asks user for name, wage,and hours worked 
name=input("Name:")
wage=input("Hourly Wage:")
wage=float(wage)
hours=input("Number of hours worked:")
hours=int(hours)

###function that calculates overtime 
def overtime_calculation(wage,hours):
    if hours>=40 and hours<=60:
        overtime=wage*1.5
        return overtime

    elif hours>60:
        overtime=wage*2+wage*1.5*20
        return overtime
 
    else:
        overtime=wage*0
        return overtime
    
#calculation that computes the pay according to the inputs hours times wage
#print statements that the user gets to see
pay=wage*hours
print("Name:",name)
print("Pay:$",pay)

#calling the function that calculates overtime 
total_pay=pay + overtime_calculation(wage,hours)
print("Total Pay:$",total_pay)

#calculation for 7% deductable for social security 
social_security=0
social_security=int(social_security)
social_security=pay*0.07
print("Social Security:$",social_security)

#15% deductable for taxes
tax=0
tax=int(tax)
tax=pay*0.15
print("Tax Withheld:$",tax)

#$30deductable for health insurance 
health_insurance=30
print("Health Insurance:$",health_insurance)

##calculation for total net pay 
net_pay=0
net_pay=int(net_pay)
#must subrtact deductables from total pay
deductable=social_security+tax+health_insurance
net_pay=total_pay-deductable
print("Net Pay:$",net_pay)
          






