try:
    temp_in_Celsius = float(input())
    print(1.8 * temp_in_Celsius + 32)
    
except ValueError:
    print("Please enter a correct number.")