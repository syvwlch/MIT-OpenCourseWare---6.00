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

# Calculating the first month
minimum_monthly_payment=minimum_monthly_payment_rate*outstanding_balance
interest_paid=annual_interest_rate/12*outstanding_balance
principal_paid=minimum_monthly_payment-interest_paid
outstanding_balance=outstanding_balance-principal_paid
