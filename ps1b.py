# Problem Set 1
# Name: Mathieu Glachant
# Collaborators: None
# Time Spent: 0:30
#

# Gathering user inputs
initial_balance=float(raw_input('Enter the outstanding balance'
                              ' on your credit card: '))
annual_interest_rate=float(raw_input('Enter the annual credit card interest rate'
                               ' as a decimal: '))
# Initialize some variables
minimum_monthly_payment=0.0
outstanding_balance=initial_balance

# Iterating until the minimum payment is sufficient to pay off the debt
while outstanding_balance>0:
    minimum_monthly_payment=minimum_monthly_payment+10.0
    outstanding_balance=initial_balance
    month=0
    # Iterating each month while it's less than a year AND the debt is not paid
    while month<12 and outstanding_balance>0:
        month=month+1
        # Calculating the month
        interest_paid=round(annual_interest_rate/12*outstanding_balance, 2)
        principal_paid=minimum_monthly_payment-interest_paid
        outstanding_balance=outstanding_balance-principal_paid

# Calculate and print the results over the year

print 'RESULT'
print 'Monthly payment to pay off debt in one year: '+str(minimum_monthly_payment)
print 'Number of months needed: '+str(month)
print 'Remaining balance: $'+str(outstanding_balance)
