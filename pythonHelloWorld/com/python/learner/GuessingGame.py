secreat_number=8
guess_limit=3
number_of_tries=0

while number_of_tries < guess_limit:
    number=input('Please guess the number ')
    if secreat_number == int(number):
        print('You guessed it right !')
        break
    else:
        print('Try Again !!')
    number_of_tries+=1
else:
    print('Sorry you failed !!')
print('DONE')
