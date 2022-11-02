from random import randint

print('Start Rock-Papper-Scissors Game')
print('Enter your choice: 0=Rock, 1=Scissors, 2=Paper')

my_hand = int(input('Enter your choice in range (0, 2): '))
pc_hand = randint(0, 2)

game_diff = my_hand - pc_hand

if game_diff== 0:
    print('Null')
elif game_diff == 1 or game_diff == -2:
    print ('lose') 
elif game_diff == -1 or game_diff == 2:
    print ('win')
