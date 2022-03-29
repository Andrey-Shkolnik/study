# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

import random
a=int(len(names))
payer=random.randint(0,a)
b=names.pop(payer)
print(f'{b} is going to buy the meal today!')