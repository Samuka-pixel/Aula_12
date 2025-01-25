from random import randint
n = randint(1, 100)
C = 1
np = 0
while np != n:
    print(C)
    np = int(input('numero de 1 a 100 '))
    if np > n:
        print('menor')
    elif np < n:
        print('maior')
    else:
        print('parabens!!')
    C = C + 1