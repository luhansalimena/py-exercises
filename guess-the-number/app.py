from random import randint

number = randint(0,10)

print("You have to guess the random number!")

def askNumber() -> int:
    return int(input("Your guess: "))


guessed_number = 0
while guessed_number != number:
    guessed_number = askNumber()
    if guessed_number == number:
        print("You guessed the right number!")
        pass
    else:
        print(f"You guessed the wrong number")


