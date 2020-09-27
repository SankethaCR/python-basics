#Tuples
number=(1,2,3,4)
print(number.index(1))
print(number)

#Unboxing
coordinates=(1,2,3)
#x=coordinates[0]
#y=coordinates[1]
#z=coordinates[2]

#print(x*y*z)
x,y,z=coordinates #Short hand form of above
print(x*y*z)

#Unboxing is not limited to tuples we can use it for List as well
number=[2,4,6,8]
a,b,c,d=number
print(a*b)