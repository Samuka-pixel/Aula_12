from random import randint
from time import sleep
Nhp = 10
Php = 10
Natk = 2
Patk = 2
while 1:
    act = str(input("Qual sera a sua ação?( A = ataque, B = Bloquear): "))

    Nact = randint(0,1)
    if Nact == 0:
        print('Inimigo atacou')
        if act == "A":
            Php = Php - Natk
        elif act == "B":
            Php = Php - (Natk/2)

    elif Nact == 1:
        if act == "A":
            Nhp = Nhp - (Patk / 2)
        elif act == "B":
            print('Inimigo Bloqueou')
            Nhp = Nhp - 0
    print(f'YOU:{Php}\n'
          f'ENEMY:{Nhp}')



    if Php == 0:
        break
    elif Nhp == 0:
        break












"""
NPCHP = 10
NPCatk = 2
PHP = 10
Patk = 2
while NPCHP > 0:
    print(f'YOU:{PHP}\n'
          f'ENEMY:{NPCHP}')
    NPCact = randint(0,1)
    if NPCact == 0:
        critdmg = randint(0,1)
        if critdmg == 1:
            NPCatk = NPCatk + +1
        PHP = PHP - NPCatk
    elif NPCact == 1:
        NPCHP = NPCHP - Patk
    sleep(3)
"""