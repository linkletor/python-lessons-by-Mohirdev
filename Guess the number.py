import random

# Generate a random number between 1 and 10

secret_number=random.randint(1,10)

print(" I am thinking of a number between 1 and 10.")

#initialize the variables 
guess = 0 
attempts = 0 

# Start the guessing loop 

while guess != secret_number:
    guess = int(input(" Entre your guess: "))
    attempts +=1 
#check the guess is correct or not 

    if guess == secret_number:
        print(f" Congrats! You guessed the number in {attempts} attempts")
    
    elif guess < secret_number:
        print(" Too low. Try again")
    else:
        print(" Too high. Try again !")
    
print(" Think any number between 1 and 10 ")
input(" Press Enter when you are ready.")
    
low = 1
high = 10
attempts = 0

while True: 
    
    guess = random.randint(low, high)
    attempts +=1
    
    print( f" Is your number {guess} ?")
    response = input(" Enter 'h' if too high , 'l' if too low  or 'c' if correct ").lower()
    
    if response == 'c':
        print(f" I guessed your number in {attempts} attempts! ")
        break
    elif response == 'h':
        high = guess -1 
    elif response == 'l':
        low = guess + 1
    else:
        print( " Please enter 'h', 'l' or 'c'.")
    
    print(" Game over!" )
        
