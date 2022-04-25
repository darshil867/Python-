import random as r

def swg(comp, mine):
    if comp == 'snake' and mine == 'gun':
        return True
    elif comp == 'water' and mine == 'snake':
        return True
    elif comp == 'gun' and mine == 'water':
        return True
    elif comp == mine:
        return None
    else:
        return False

choice = ('snake', 'water', 'gun')
comp = choice[r.randint(0, 2)]
# comp = choice[comp]

mine = input('Enter your choice as snake, water or gun: ')

win = swg(comp, mine)
print(f'You choose {mine} and the computer choose {comp}')

if win is None:
    print('Match Drawn')
elif win:
    print('You won')
else:
    print('You lose')
