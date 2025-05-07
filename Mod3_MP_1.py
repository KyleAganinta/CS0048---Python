
#Calculator Fucnction

def add(a, b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    return a/b

print ("Welcome to calculator machine!")
while True:
    print ("Please select your operation")
    print ("1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Exit")

    choice = int(input ("Input your choice divided by: "))
    num1 = None
    num2 = None

    if choice == 1:
        num1, num2 = map(int, input("Input the numbers you would want to add divided by a space: ").split(" "))
        print ("sum = ", add(num1, num2))
    
    elif choice == 2:
        num1, num2 = map(int, input("Input the numbers you would want to subtract divided by a space: ").split(" "))
        print ("difference = ", subtract(num1, num2))

    elif choice == 3:
        num1, num2 = map(int, input("Input the numbers you would want to multiply divided by a space: ").split(" "))
        print ("product = ", multiply(num1, num2))

    elif choice == 4:
        num1, num2 = map(int, input("Input the numbers you would want to divide, divided by a space: ").split(" "))
        print ("quotient = ", divide(num1, num2))

    elif choice == 5:
        break

    else:
        print("Invalid inpt")

print("Thank you for using my calculator")

