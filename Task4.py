"""Write a program which, based on the variables: amount - amount (float) and number of installments - number_of_installments (int), will calculate the monthly loan installment and write it to the console. The parameters have restrictions:

the loan amount must be between PLN 100.00 and PLN 10,000.00,
the number of installments must be between 6 and 48.
If the loan amount exceeds the acceptable range, the loan amount should be set at PLN 5,000.00. If the number of installments exceeds the acceptable range, the number of installments should be set to 36.

The calculated monthly installment should also include interest. To simplify the calculations, assume that you add X percent to the loan amount depending on the number of installments:

6-12 installments - 2.5%,
13-24 installments - 5.0%,
25-48 installments - 10.0%,
and then calculate the installment amount based on the number of installments.

Get data from the user in the console using argument-less input()."""

try:
    loan_amount = float(input())
    number_of_installments = int(input())
# Loan amount
    if loan_amount < 100.00:
        loan_amount = 5000.00
    if loan_amount > 10000.00:
        loan_amount = 5000.00

# Installments
    if number_of_installments < 6:
        number_of_installments = 36
    if number_of_installments > 48:
        number_of_installments = 36
    
# Code to calculate %
    if number_of_installments < 13:
        loan_amount = loan_amount + (loan_amount / 100 * 2.5)
    elif number_of_installments >= 13 and number_of_installments < 25:
        loan_amount = loan_amount + (loan_amount / 100 * 5)
    else:
        loan_amount = loan_amount + (loan_amount / 100 * 10)
# Calculating installments 
    installments = loan_amount / number_of_installments
    print(installments)
except:
    print("Incorrect values entered!")

    
