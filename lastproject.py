import random
def user_name():
    #Ask the user for name.
    name = input(" What is your name? ")
    reversed_name = name[::-1]

    #generate a random number between 0 and 9
    random_number = random.randint(0,9)

    #combine the user_name with random number 
    username = reversed_name +  str(random_number)

    return f" Generated username for you: {username}"

print(user_name())



