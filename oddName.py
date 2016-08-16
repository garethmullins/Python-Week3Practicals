name = input("Please enter your name. ")
while any(i.isdigit() for i in name):
    name = input("The name entered contained a number, please renter your name. ")
temp = 0
for i in name:
    temp += 1
    if temp % 2 == 1:
        print(i, end=" ")