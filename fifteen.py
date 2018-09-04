import random
empty_cell = ' x '
win_shield = [[' 1 ', ' 2 ', ' 3 ', ' 4 '], [' 5 ', ' 6 ', ' 7 ', ' 8 '], [' 9 ', '10 ', '11 ', '12 '], ['13 ', '14 ', '15 ', empty_cell]]
first_list = [' 1 ', ' 2 ', ' 3 ' , ' 4 ', ' 5 ', ' 6 ', ' 7 ', ' 8 ', ' 9 ', '10 ', '11 ', '12 ', '13 ', '14 ', '15 ', empty_cell]
random.shuffle(first_list)

game_shield = []
for i in range(len(first_list)//4):
    game_shield.append(first_list[i*4:i*4+4])
if len(first_list) % 4 > 0:
    game_shield.append(first_list[-1*(len(first_list)%4):])

def new_shield():
    if game_shield == win_shield:
        print('You won')
    print('\n',game_shield[0],'\n',game_shield[1],'\n',game_shield[2],'\n', game_shield[3],'\n')
    for x in range(0, len(game_shield)):
        for y in range(0, len(game_shield[x])):
            if game_shield[x][y] == empty_cell:
                a = x
                b = y
                break
    hod = str(input('Vash hod: '))
    try:
        if hod != 'w' and hod != 's' and hod !=  'd' and hod != 'a':
            raise ValueError('Ne pravilny hod')
    except ValueError:
        print('Wrong input')
        new_shield() 
    return new_hod(hod, a, b)

def new_hod(hod, a, b):
            
    if hod == 'w':
        try:
            if a-1 < 0:
                raise TypeError()
        except TypeError:
             print('Out of Range!!!')
             new_shield()
 
        game_shield[a][b], game_shield[a-1][b] = game_shield[a-1][b], game_shield[a][b]
        new_shield()

    if hod == 's':
        try:
            if a+1 > 3:
                raise TypeError()
        except TypeError:
             print('Out of Range!!!')
             new_shield()

        game_shield[a][b], game_shield[a+1][b] = game_shield[a+1][b], game_shield[a][b]
        new_shield()

    if hod == 'a':
        try:
            if b-1 < 0:
                raise TypeError()
        except TypeError:
             print('Out of Range!!!')
             new_shield()

        game_shield[a][b], game_shield[a][b-1] = game_shield[a][b-1], game_shield[a][b]
        new_shield()

    if hod == 'd':
        try:
            if b+1 > 3:
                raise TypeError()
        except TypeError:
             print('Out of Range!!!')
             new_shield()

        game_shield[a][b], game_shield[a][b+1] = game_shield[a][b+1], game_shield[a][b]
        new_shield()
new_shield()


