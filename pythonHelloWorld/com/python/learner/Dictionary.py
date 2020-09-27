customer ={
    "name":"Jonh Smith",
    "age":30,
    "is_verified":True
}
#Key should be unique
print(customer["name"])
print(customer.get("Name")) #None
customer["name"]="Sanketh"
print(customer.get("dateOfBirth"),"03-10-1990")
print(customer["name"])

#Exercise
NumberToString={
    "0":"Zero",
    "1":"One",
    "2":"Two",
    "3":"Three",
    "4":"Four",
    "5":"Five",
    "6":"Six",
    "7":"Seven",
    "8":"Eight",
    "9":"Nine"
}
number=input('Please enter the Phone number!! ')
for num in range(0,len(number)):
    print(NumberToString[number[num]],end=' ')

#Excercise on Emoji
emoji={
    ":)":"Happy",
    ":(":"Sad"
}
print()
message=input('Enter the message > ')
output=''
words=message.split(' ')
for word in words:
    output+=emoji.get(word,word)+" "
print(output)
