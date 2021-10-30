try:
    height = int(input("Please enter your height: "))
    weight = int(input("Please enter your weight: "))

    if height > 150 and weight < 180:
        print("Fasten seat belts!")
    else:
        print("I'm sorry you can't ride!")
except:
    print("Enter numerical values only")