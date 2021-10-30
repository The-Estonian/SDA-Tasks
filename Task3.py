try:
    income = float(input())
    if income <= 8552800:
        income = (income - 556.02) / 100 * 18
        print(income)
    else:
        income = (income - 1483902) / 100 * 32 + 1483902
        print(income)









except ValueError:
    print("Bad bad value")