for x in range(4):
    for y in range(3):
        print(f"({x},{y})")

# Exercise Print F
print('=========================')
numbers=[5,2,5,2,2]
count= 1
for count_x in numbers:
    count=''
    for y in range(count_x):
        count+='X'
    print(count)


# Exercise Print L
print('=========================')
numbers=[2,2,2,2,5]
count= 1
for count_x in numbers:
    count=''
    for y in range(count_x):
        count+='X'
    print(count)

# Exercise on Python list
names=['sanketh','samip','samrat','virat','vikram']
print(names[:]) #Print all the values in the list
print(names[1:-1]) #Print from index 1 to last but one
print(names[2:]) #Print from 2nd index
print(names[-1])
print(names[-2])

#Modify
names[0]='sanketha'
print(names)

#Largest number in the list
numbers=[1,5,6,19,12,3,4]

for num in numbers:
    print(num)
print('==================')

large = numbers[0]
for num in numbers:
   # print(large)
    if large < num:
        large=num
print('Largest number')
print(large)
print('=========================')

