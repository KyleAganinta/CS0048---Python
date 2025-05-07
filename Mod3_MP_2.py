

def CtoF (a):
    return a*(9/5) + 32 

def FtoC (a):
    return (a-32)*(5/9) 


while True:
    print ("Welcome to temperature converter\nMenu:\n1. Celsius to Farenheit\n2. Farenheit to Celsius\n3. Exit")

    choice = int(input("Input your choice: "))
    num1 = None
    temp = None
    if choice == 1:
        num1 = float(input("Input your temperature in celsius: "))
        temp = CtoF(num1)
        print (f"{num1} Celcius to FArenheit is {temp:.2f}")
    
    if choice == 2:
        num1 = float(input("Input your temperature in celsius: "))
        temp = FtoC(num1)
        print (f"{num1} Farenheit to Celsius is {temp:.2f}")
    if choice == 3:
        break

print("\n\nThanks for using Temperature Calculator")
