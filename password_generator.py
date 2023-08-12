import random
char = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@#$%^&*[]"
while True:
    len = int(input("Enter the length of required password :- "))
    count = int(input("Enter the number of required password :- "))

    for i in range(0,count):
        password = ""
        for j in range(0,len):
            pass_char = random.choice(char)
            password += pass_char
        print("The generated password is",password)
    repeat = input("Do you want to generate more passwords ? ")
    if repeat == "no" or repeat == "NO":
        break

print("Thank You!")
  