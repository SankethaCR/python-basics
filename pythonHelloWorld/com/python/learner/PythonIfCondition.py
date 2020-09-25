is_hot =False
is_cold =False

if is_hot:
    print("Today is hot day")
    print("Drink more water")
elif is_cold:
    print("Today is cold day")
    print("Wear jacket")
else:
    print("Today is lovely Day !!")
print("Enjoy your day !")

house_price=10000
credit_limit='Good'

if credit_limit:
    pay=int(house_price)*1.0
    print(f'You need to pay [{pay}]')
    print(pay)
else:
    pay=int(house_price)*0.2
    print('You need to pay [{pay}]')
print("Success  !!!")