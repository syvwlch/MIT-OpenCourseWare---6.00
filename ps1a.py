# Problem Set 1
# Name: Mathieu Glachant
# Collaborators: None
# Time Spent: 0 (started 12:15 on Friday)
#

# Gathering user inputs
outstanding_balance=float(raw_input('Enter the outstanding balance'
                              ' on your credit card: '))
annual_interest_rate=float(raw_input('Enter the annual credit card interest rate'
                               ' as a decimal: '))
minimum_monthly_payment_rate=float(raw_input('Enter the minimum monthly payment rate'
                                       ' as a decimal: '))

# Iterating the calculation and display of the results
for month in range(1,13):
    # Calculating the month
    minimum_monthly_payment=round(minimum_monthly_payment_rate
                                  *outstanding_balance, 2)
    interest_paid=round(annual_interest_rate/12*outstanding_balance, 2)
    principal_paid=minimum_monthly_payment-interest_paid
    outstanding_balance=outstanding_balance-principal_paid

    # Printing the month
    print 'Month: '+str(month)
    print 'Minimum monthly payment: $'+str(minimum_monthly_payment)
    print 'Principle paid: $'+str(principal_paid)
    print 'Remaining balance: $'+str(outstanding_balance)
