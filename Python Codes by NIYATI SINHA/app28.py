#while loops have a else part as well in Python
#guess the secret number within 3 turns
secret_number=9
guess_count=0
guess_limit=3
while guess_count<guess_limit:
    guess=int(input('Guess: '))
    if guess==secret_number:
        print("You Win")
        break
    guess_count+=1
else: #comes to this part after the condition of while becomes false
    print("Sorry, You lost! You exhausted all three turns.")