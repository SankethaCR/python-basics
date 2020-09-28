try:
    age = int(input('Enter the Age'))
    print(f'Age = {age}')
    dAge=age/0
except ValueError:
    print('Invalid Value! Please enter valid Age !')
except ZeroDivisionError:
    print('We should not devide by ZERO !')