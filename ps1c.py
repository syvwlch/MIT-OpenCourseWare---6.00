# Problem Set 1
# Name: Mathieu Glachant
# Collaborators: None
# Time Spent: 0:56
#

# Gathering user inputs
initial_balance=float(raw_input('Enter the outstanding balance'
                              ' on your credit card: '))
annual_interest_rate=float(raw_input('Enter the annual credit card interest rate'
                               ' as a decimal: '))
# Initialize some variables
lower_bound_monthly_payment=initial_balance/12.0
upper_bound_monthly_payment=(
    initial_balance*(1+(annual_interest_rate/12))**12.0)/12.0
outstanding_balance=initial_balance

# Iterating until the minimum payment is enough to pay the debt in one year
while upper_bound_monthly_payment-lower_bound_monthly_payment>=0.01:
    minimum_monthly_payment=(
        (lower_bound_monthly_payment+upper_bound_monthly_payment)/2.0)
    outstanding_balance=initial_balance
    month=0
    # Iterating each month while it's less than a year
    for month in range(1,13):
        # Calculating the month
        interest_paid=round(annual_interest_rate/12*outstanding_balance, 2)
        principal_paid=minimum_monthly_payment-interest_paid
        outstanding_balance=outstanding_balance-principal_paid
    # check to see if we are over or under the ideal value
    if outstanding_balance>0:
        lower_bound_monthly_payment=minimum_monthly_payment
    else:
        upper_bound_monthly_payment=minimum_monthly_payment
    
# Calculate and print the results over the year

print 'RESULT'
print 'Monthly payment to pay off debt in one year: '+str(
            round(minimum_monthly_payment, 2))
print 'Number of months needed: '+str(month)
print 'Remaining balance: $'+str(
            round(outstanding_balance, 2))
