try :
    import random

    random_number = random.randint(1, 100)
    attept_call = 3


    def correct_guess(user_guess):
        if user_guess == random_number :
            print("="*40)
            print("Thats correct answer!!!!!")
            print("="*40)
        
    def users_guesses(user_guess):
        if user_guess < random_number :
            return "Number is small"
                
        if user_guess > random_number:
            return "Number is large"



    def attept_over(attept_call):
        if attept_call == 0:
            print('-' * 40)
            print("Attept is over")
            return "YOU LOOOSE"

    while attept_call > 0 :
        user_guess = int(input("Enter the number; "))
        if user_guess == random_number :
            print(correct_guess(user_guess))
            break
        
        if user_guess < random_number or user_guess > random_number :
            print(users_guesses(user_guess))
            attept_call = attept_call - 1
            print(f"{attept_call} Attept Left...")
            
        if attept_call == 0 :
            print(attept_over(attept_call))
            
except ValueError as error:
    print(f"Failed to convert input: {error}")