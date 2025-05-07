import random

print ("Welcome to numbers guessing game\nMenu: \n1. Play\n2. Exit")
random_number = random.randint(1, 10)

choice = int(input("input your choice: "))

while True:
    if choice == 1:
        guess = None
        counter = 1
        while guess!=random_number:
            guess = int(input("Kindly input your guess: "))
            if guess > random_number:
                print ("Guess Lower")
                counter+=1
            elif guess < random_number:
                print ("Guess Higher")
                counter+=1

        else:
            print(f"You got it right in just {counter} tries")
            break

    elif choice == 2:
        break

    else:
        print("Invalid input")

print("Thanks for playing!")    
