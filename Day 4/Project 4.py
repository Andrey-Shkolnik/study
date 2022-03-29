rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

import random
player=int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.'))
computer=random.randint(0,2)
if player==0 and computer==0:
    print ("Draw")
    print (f'Player choose\n{rock}')
    print (f'Computer choose\n{rock}')
if player==1 and computer==1:
    print("Draw")
    print(f'Player choose\n{paper}')
    print(f'Computer choose\n{paper}')
if player==2 and computer==2:
    print("Draw")
    print(f'Player choose\n{scissors}')
    print(f'Computer choose\n{scissors}')
if player==0 and computer==1:
    print ("Computer wins")
    print(f'Player choose\n{rock}')
    print(f'Computer choose\n{paper}')
if player==1 and computer==2:
    print ("Computer wins")
    print(f'Player choose\n{paper}')
    print(f'Computer choose\n{scissors}')
if player==2 and computer==0:
    print ("Computer wins")
    print(f'Player choose\n{scissors}')
    print(f'Computer choose\n{rock}')
if player==0 and computer==2:
    print ("Player wins")
    print(f'Player choose\n{rock}')
    print(f'Computer choose\n{scissors}')
if player==1 and computer==0:
    print ("Player wins")
    print(f'Player choose\n{paper}')
    print(f'Computer choose\n{rock}')
if player==2 and computer==1:
    print ("Player wins")
    print(f'Player choose\n{scissors}')
    print(f'Computer choose\n{paper}')
