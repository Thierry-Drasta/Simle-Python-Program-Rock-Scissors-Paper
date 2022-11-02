import random

def start_message():
    print('start Rock-Papper-Scissors Game')
    print('choice: 0=Rock, 1=Scissors, 2=Paper')
    print('________________________________________________')
    
def get_player():
    my_hand = int(input('Enter your choice in range (0, 2): '))
    return my_hand

def get_pc():
    pc_hand = random.randint(0, 2)
    return pc_hand

def view_result(hand_diff):
    
    if hand_diff == 0:
        print('Null')
    elif hand_diff == 1 or hand_diff == -2:
        print ('lose') 
    elif hand_diff == -1 or hand_diff == 2:
        print ('win')
        

start_message()
view_result(get_player() - get_pc())