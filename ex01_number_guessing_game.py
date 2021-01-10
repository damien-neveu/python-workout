import random

if __name__ == "__main__":
    secret_num = random.randint(0, 100)
    secret_num_found = False
    while not secret_num_found:
        str_guess_num = input("What is your guess for the secret number (between 0 and 100) ?")
        if str_guess_num.isnumeric():
            guess_num = int(str_guess_num)
            if guess_num < secret_num:
                print("Too low")
            elif guess_num > secret_num:
                print("Too high")
            else:
                print("Just right")
                secret_num_found = True
        else:
            print(f"\"{str_guess_num}\" is not a valid number")
    print("Thanks for playing !")
