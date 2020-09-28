def first_function(first_name,last_name): #Position arguments
    print(f'Welcome to Python function {first_name} {last_name}')
    print('Function world !')


print('Start Function!')
first_function("John","Smith")
first_function(last_name="Cr",first_name="Sanketh") #Keyword argument
first_function("Sanketh",last_name="CR")
print('End !')

#Return stattement

def square(number):
    return (number*number)

number=3
print(f'Square of {number} is {square(3)}')

#By default it will return 'None' if you don't want to return 'None' then you need to return value
