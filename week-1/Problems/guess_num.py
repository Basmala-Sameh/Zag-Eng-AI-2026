secret = 7
repeat = True

while repeat==True :
    guess = int(input("Guess the secret number \n"))

    if guess == secret:
        print("Congratulations!\nYou guessed the right number")
        repeat = False
    else:
        print("Hard luck!\nYour guess was wrong\ntry again")
        again = input("Want to try again ? (y/n)").lower().strip()
        if again == "n" :
            repeat = False 


