import random

print ("Welcome to numbers guessing game\nMenu: \n1. Play\n2. Exit")




while True:
    choice = int(input("input your choice: "))
    if choice == 1:
        random_number = random.randint(1, 10)
        guess = None
        counter = 1
        while guess!=random_number:
            guess = int(input("Kindly input your guess: "))
            if guess > random_number:
                print ("Lower!")
                counter+=1
            elif guess < random_number:
                print ("Higher!")
                counter+=1     
        print(f"You got it right in just {counter} tries")
        break
        

    elif choice == 2:
        break

    else:
        print("Invalid input")

print("Thanks for playing!")    
