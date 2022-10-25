import random
print("Welcome to number guess!")
range = int(input("enter the maximum number allowed: "))
allow = int(input("how many guesses are allowed? ")) + 0.1

number = random.randrange(range)

loop = int(1)

while allow > loop:
    x = int(input("guess: "))
    if x == number:
        print("correct")
        quit()
    else:
        print("Incorrect.")
        loop = (loop + 1)
print("GAME OVER")
quit()
