from random import randint


print('Start Rock-Papper-Scissors Game')
print('Enter your choice: 0=Rock, 1=Scissors, 2=Paper')

my_hand = int(input('Enter your choice in range (0, 2): '))
pc_hand = randint(0, 2)

if my_hand == 0:
    if pc_hand == 0:
        print('Null')
    elif pc_hand == 1:
        print ('lose') 
    elif pc_hand == 2:
        print ('win')   

elif my_hand == 1:
    if pc_hand == 0:
        print('lose')
    elif pc_hand == 1:
        print('Null')
    elif pc_hand == 2:
        print('win')
        
elif my_hand == 2:
    if pc_hand == 0:
        print('win')
    elif pc_hand == 1:
        print('lose')
    elif pc_hand == 2:
        print('Null')
        
        