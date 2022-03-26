# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

both_names=name1.lower()+name2.lower()
true=both_names.count('t')+both_names.count('r')+both_names.count('u')+both_names.count('e')
love=both_names.count('l')+both_names.count('o')+both_names.count('v')+both_names.count('e')
score=int(true*10+love)
if score<10 or score>90:
    print (f"Your score is {score}, you go together like coke and mentos.")
elif score>=40 and score<=50:
    print (f"Your score is {score}, you are alright together.")
else:
    print (f'Your score is {score}.')