import random
def play():
    user=input("'r' for rock, 'p' for paper, 's' fpr scissors\n")
    computer = random.choice(['r','p','s'])

    if user == computer:
        return 'it is a tie'


    if is_win(user,computer):
        return 'you won'

    return 'you lost'


    def is_win(p,o):
        if(p == 'r' and o == 's') or (p=='s' and o == 'p') or (p == 'p' and o == 'r'):
            return true
print(play())