def add(x,y):
    return x +y
#addition

def sub (x,y):
    return x - y
# sub

def division (x,y):
    return x/y

def times(x,y):
    return x*y

print("Select the operation")
print("1.Add")
print("2.Sub")
print("3.times")
print("4.Divide")

while True:
    #take input
    choice = input("Enter choice(1/2/3/4): ")

    #check the choice
    if choice in ('1','2','3','4'):
        try:
            num1 = float(input("Enter first number"))
            num2 = float(input("Enter second number"))
        except ValueError:
            print("Invalid  input. Please enter number")
            continue
        if choice == '1':
            print(num1, "+", num2, "=", add(num1,num2))
        
        elif choice  == '2':
            print(num1, "-", num2, "=",sub(num1,num2))

        elif choice == '3':
            print(num1, "*", num2, "=",times(num1,num2))
        
        elif choice == '4':
            print(num1, "/", num2, "=", division(num1,num2))
        next_calcuation = input("Lets do an another one")
        if next_calcuation == 'no':
            break
else:
    print("Invalid input")
