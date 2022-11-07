secret_word = "Medicine" 

user_guess = input("Enter Guess: ").capitalize()

tries = 4


while secret_word != user_guess:

    tries -= 1

    if tries > 1:

        print(f'Wrong Guess, {tries} chances left')

    elif tries == 1:

        print('Wrong Guess, last chance left')

    elif tries == 0:

        print('All chances are finished!')

        break

    user_guess = input("Enter Guess: ").capitalize()


else:

    print("You Win")



