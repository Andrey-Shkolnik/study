# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
if year/4==year//4:
    if year/100==year//100:
        if year/400==year//400:
            print ('leap')
        else:
            print ('not leap')
    else:
        print ('leap')
else:
    print('not leap')