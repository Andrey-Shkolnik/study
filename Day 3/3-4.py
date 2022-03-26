# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆
#Small Pizza: $15
#Medium Pizza: $20
#Large Pizza: $25
#Pepperoni for Small Pizza: +$2
#Pepperoni for Medium or Large Pizza: +$3
#Extra cheese for any size pizza: + $1
#Write your code below this line 👇
total=0
if size=='S':
    if add_pepperoni=='Y':
        if extra_cheese=='Y':
            total=15+2+1
            print (f'Your final bill is: ${total}')
        else:
            total=15+2
            print (f'Your final bill is: ${total}')
    else:
        total=15
        print (f'Your final bill is: ${total}')
elif size=='M':
    if add_pepperoni=='Y':
        if extra_cheese=='Y':
            total=20+3+1
            print (f'Your final bill is: ${total}')
        else:
            total=20+3
            print (f'Your final bill is: ${total}')
    else:
        total=20
        print (f'Your final bill is: ${total}')
elif size=='L':
    if add_pepperoni=='Y':
        if extra_cheese=='Y':
            total=25+3+1
            print (f'Your final bill is: ${total}')
        else:
            total=25+3
            print (f'Your final bill is: ${total}')
    else:
        total=25
        print (f'Your final bill is: ${total}')
else:
    print ('Enter correct data')