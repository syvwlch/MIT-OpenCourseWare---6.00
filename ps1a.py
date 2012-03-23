# Problem Set 1
# Name: Mathieu Glachant
# Collaborators: None
# Time Spent: 0:53
#

# Gathering user inputs
outstanding_balance=float(raw_input('Enter the outstanding balance'
                              ' on your credit card: '))
annual_interest_rate=float(raw_input('Enter the annual credit card interest rate'
                               ' as a decimal: '))
minimum_monthly_payment_rate=float(raw_input('Enter the minimum monthly payment rate'
                                       ' as a decimal: '))

# Iterating the calculation and display of the results
total_amount_paid=0.0
for month in range(1,13):
    # Calculating the month
    minimum_monthly_payment=round(minimum_monthly_payment_rate
                                  *outstanding_balance, 2)
    interest_paid=round(annual_interest_rate/12*outstanding_balance, 2)
    principal_paid=minimum_monthly_payment-interest_paid
    outstanding_balance=outstanding_balance-principal_paid
    total_amount_paid=total_amount_paid+minimum_monthly_payment

    # Printing the month
    print 'Month: '+str(month)
    print 'Minimum monthly payment: $'+str(minimum_monthly_payment)
    print 'Principle paid: $'+str(principal_paid)
    print 'Remaining balance: $'+str(outstanding_balance)

# Calculate and print the results over the year

print 'RESULT'
print 'Total amount paid: $'+str(total_amount_paid)
print 'Remaining balance: $'+str(outstanding_balance)
