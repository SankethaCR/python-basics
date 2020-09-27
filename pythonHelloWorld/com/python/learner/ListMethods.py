number = [5,2,1,7,4]
number.append(20)
number.insert(2,30) #Insert at index 2
#number.clear()
print(f'Length of list = {len(number)}') #Length of List, len is the generic method
print(number)
number.pop()
print(number)
print(number.index(2))
print(50 in number)
number.sort()
print(number)
number.reverse()
print(number)

numbers2=number.copy()
numbers2.append(100)
print(f'Number1 list {number}')
print(f'Number2 list {numbers2}')

print('============== Remove duplicates in the list ============ ')
numberList=[3,2,3,4,5,6,9,2]
uniqueList=[]
print(numberList)
for x in numberList:
    if x not in uniqueList:
        uniqueList.append(x)
print(uniqueList)


