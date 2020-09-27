for item in 'Python':
    print(item)

for items in ['sanketh','cr','rockstar']:
    print(items)
for item in range(10):
    print(item)
print('======================')
for item in range(5,10):
    print(item)
print('=============')

for item in range(5,10,2):
    print(item)

print('Exercise on For Loop ') # Exercise
prices=[10,20,30,40]
count=0
for items in range(0,len(prices)):
    count+=prices[items]
print(f'Total price =  {count}')