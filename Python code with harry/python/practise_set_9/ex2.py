import random as r

def game():
    score = r.randint(1, 100)
    print(f'The score is {score}')
    return score

score = game()

with open('Highscore.txt', 'r') as f:
    highscore = int(f.read())

if score > highscore:
    with open('Highscore.txt', 'w') as f:
        f.write(str(score))
