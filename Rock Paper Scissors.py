import random



def play():
    user = input("Whats your choice ?'r' for rock,'p' for paper,'s'for scissors\n")
    computer = random.choice(['r' , 's' , 'p'])
    if  user == computer:
        return 'Tie'
    if Is_Win(user,computer):
        return 'You Won'
    else:
        return 'You Lost'

def Is_Win(player,opponent):
    if (player == 'r' and opponent =='s') or (player == 's' and opponent == 'p')\
         or (player == 'p' and opponent == 'r'):
        return True


print(play())

