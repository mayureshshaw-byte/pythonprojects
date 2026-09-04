import random
input= input ("click Y/N to generate your password   ")
string="qwertyuiopasdfghjklzxcvbnm"
sign="!@#$%^&*YY"
num="1234567890"
n=0
password=""
while n<3:
    if input=="Y":
        password = password +random.choice(string)
        password = password +random.choice(sign)
        password = password +random.choice(num)
        n=n+1
    else:
        print("no password ")
        break

print(f"your password is {password:^10}")