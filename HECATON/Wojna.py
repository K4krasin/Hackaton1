# Zasady: https://pl.wikipedia.org/wiki/Wojna_(gra_karciana)
# Konieczność użycia modułu random.
# Program rozdaje karty i drukuje informacje o przebiegu rozgrywki
# Pomysły na uproszczenie gry:
# zamiast implementować talię kart, używamy liczb (0, 1, 2 ... 9, 10, 11) dla (2, 3, 4, ... Q, K, A)
# aby gra kończyła się wcześniej, rozdajemy tylko 10 kart
# dwa tryby: zdobyte karty dochodzą do "ręki", lub są odkładane i nie wykorzystywane

import random
cards = [1,2,3,4,5,6,7,8,9,10,11,12,13,1,2,3,4,5,6,7,8,9,10,11,12,13,1,2,3,4,5,6,7,8,9,10,11,12,13,1,2,3,4,5,6,7,8,9,10,11,12,13]

player1 = []
player2 = []


def wojna (karta1, karta2):
    for n in range(2,10,2):
        if len(karta1) < 3:
            k = karta1[-1]
        else:
            k = karta1[2]
        if len(karta2) < 3:
            k1 = karta2[-1]
        else:
            k1 = karta2[2]
        print(k, k1)
        if k > k1:
            karta1.extend(karta2[0:2])
            karta1.extend(karta1[0:2])
            del karta2[0:2]
        elif k < k1:
            karta2.extend(karta1[0:2])
            karta2.extend(karta2[0:2])
            del karta1[0:2]
        else:
            n += 2
        return karta1, karta2

def winner (len1,len2):
    if len(player1) == 0:
        return print("Wygrywa gracz 2")
    else:
        return print("Wygrywa gracz 1")


for i in range(0,10):
    select_card = random.choice(cards)
    player1.append(select_card)
    cards.remove(select_card)
    select_card = random.choice(cards)
    player2.append(select_card)
    cards.remove(select_card)
print("karty gracza 1 :",player1)
print("karty gracza 2 :",player2)


while (len(player1) > 1 or (len(player2) > 1)):
    if len(player1) == 0 or (len(player2) == 0):
        break
    if player1[0] > player2[0]:
        print(player1[0], player2[0])
        player1.append(player1[0])
        player1.append(player2[0])
        player1.remove(player1[0])
        player2.remove(player2[0])
    elif player1[0] < player2[0]:
        print(player1[0], player2[0])
        player2.append(player1[0])
        player2.append(player2[0])
        player2.remove(player2[0])
        player1.remove(player1[0])
    else:
        wojna(player1, player2)
    print("karty gracza 1 :", player1)
    print("karty gracza 2 :", player2)


winner(player1,player2)

