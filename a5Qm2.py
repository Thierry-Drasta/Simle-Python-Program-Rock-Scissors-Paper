import random

def start_message():
    print('start Rock-Papper-Scissors Game')
    print('choice: 0=Rock, 1=Scissors, 2=Paper')
    
def get_player():
    print('Input Your Hand')
    
    # return statement to input and display the message of urgue to input the hand
    return int(input('Enter your choice in range (0, 2): '))

def get_pc():
    
    # Return statement to Computer hand's value
    return random.randint(0, 2)

def view_result(hand_diff):
    
    if hand_diff == 0:
        print('Null')
    elif hand_diff == 1 or hand_diff == -2:
        print ('lose') 
    elif hand_diff == -1 or hand_diff == 2:
        print ('win')
        

start_message()

my_hand = get_player()
your_hand = get_pc()
hand_diff = my_hand - your_hand

view_result(hand_diff)