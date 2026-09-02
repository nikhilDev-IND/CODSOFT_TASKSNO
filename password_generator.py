import string
import random
letters=string.ascii_letters
alphanum=string.ascii_letters+ string.digits 
characters=string.ascii_letters + string.punctuation + string.digits 
print("<<<< Welcome to the Password generator>>>>")
while True:
    try:
        length=int(input("Enter the length you want for your password : "))
        if length>0:
            break
        else:
            print("Please enter a positive number.")
    except ValueError:
        print("Please enter a positive number.")

print("Select the difficult level from : ")
print('(a) Easy')
print("(b) Hard")
print("(c) Difficult")

while True:
    try:
        difficulty=input("enter the diffuculty level : ").lower()
        if difficulty in ('a','b','c'):
            break
        else:
            print("Please enter a ,b or c.")
    except ValueError :
        print("Please enter a,b or c")
password=""

if difficulty=="c":
    for i in range(length):
        password+=random.choice(characters)
elif difficulty=='a':
    for i in range(length):
        password+=random.choice(letters)
elif difficulty=='b':
        for i in range(length):
            password+=random.choice(alphanum)
print('The password generated is : ',password)


