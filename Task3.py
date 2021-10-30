try:
    income = float(input())
    if income <= 85528.00:
        income = (income / 100 * 18) - 556.02
        if income < 0:
            income = 0
            print(income)
        else:
            print(income)
    else:
        income = (income - 85528.00) / 100 * 32 + 14839.02
        print(income)

except:
    print("Please enter the value in numbers.")