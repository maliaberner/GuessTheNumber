def generate_num():
    from random import randint
    global num_to_guess
    num_to_guess = randint(0,1000000)
    #print(num_to_guess)

def check_num():
    num_guessed = input('Guess the number')
    #print(num_to_guess)
    while num_guessed != num_to_guess:
        if num_guessed > num_to_guess:
            print('Lower')
        elif num_guessed < num_to_guess:
            print('Higher')
        num_guessed = input('Guess the number')

    if num_guessed == num_to_guess:
        print('Good job!')

generate_num()

check_num()
