# Problem Set 1
# Name: Mathieu Glachant
# Collaborators: None
# Time Spent: Started 14:15 on Friday
#

# Gathering user inputs
outstanding_balance=float(raw_input('Enter the outstanding balance'
                              ' on your credit card: '))
annual_interest_rate=float(raw_input('Enter the annual credit card interest rate'
                               ' as a decimal: '))
# Initialize some variables
minimum_monthly_payment=10.0

# Iterating the calculation and display of the results
for month in range(1,13):
    # Calculating the month
    interest_paid=round(annual_interest_rate/12*outstanding_balance, 2)
    principal_paid=minimum_monthly_payment-interest_paid
    outstanding_balance=outstanding_balance-principal_paid

# Calculate and print the results over the year

print 'RESULT'
print 'Monthly payment to pay off debt in one year: '+str(minimum_monthly_payment)
print 'Number of months needed: '+str(1)
print 'Remaining balance: $'+str(outstanding_balance)
