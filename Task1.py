try:
    height = int(input().strip("cm"))

    weight = float(input().strip("kg"))

    if height >= 150 and weight <= 180:
        print("Fasten seat belts!")
    else:
         print("I'm sorry you can't ride!")
except:
    print("Oops, there seems to have been an error entering values. \
Please enter Height in cm and Weight in kg!")