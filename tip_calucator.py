print("Welcome to the tip calucator!")
bill = float(input("What was the total bill?"))
tip = float(input("What percentage tip would you like to give ? 10,12, or 18?"))
tip1 = 1 + (tip /100)

split =float(input("How many people are going to split the bill?"))
amount = round((bill/ split) * tip1,2)
print(f"Each person should pay: {amount}")