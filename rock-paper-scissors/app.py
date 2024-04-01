import random

wins = {
    "R": "S",
    "P": "R",
    "S": "P"
}

def play():
    print('[R] for Rock | [P] for Paper | [S] for Scissors');
    computer_play = random.choice(['R','P','S']);
    user_play = input();
    print(f'Computer played: {computer_play}')
    if(user_play == computer_play):
        return print('Tie!')
    
    if(user_play == wins[computer_play]):
        return print('You lose!')
    
    return print('You Win!')

play()