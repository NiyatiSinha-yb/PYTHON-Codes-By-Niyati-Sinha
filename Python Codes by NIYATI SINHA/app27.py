#guess the secret number within 3 turns
secret_number=9
guess_count=0
guess_limit=3
flag=0
while guess_count<guess_limit:
    guess=int(input('Guess: '))
    if guess==secret_number:
        print("You Win")
        flag=1
    else:
        print("You lost")
    guess_count+=1 #guess_count++ will give error
    if flag==1 :
        break
