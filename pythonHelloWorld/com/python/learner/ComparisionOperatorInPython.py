temperature=30
if temperature > 30: # == , !=,
    print('its hot day !')
else:
    print('it is not hot day !')

print('=============================================')
name=input('Please enter your name .. ')
name_len=len(name)
if name_len <= 3:
    print('Name should be gretter thant 3 charecter !')
elif name_len >=50:
    print('Name length should be less than 50')
else:
    print('Name looks Good !!!')
