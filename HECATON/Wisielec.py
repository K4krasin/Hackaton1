# Wisielec:
# Program, będący implementacją gry "wisielec".
#
# Użytkownik ma za zadanie odgadnąć hasło, które ukryte jest w programie.

# Program pokazuje ile liter ma hasło i te litery, które zostały już odgadnięte

# Użytkownik podaje po jednej literze. Użytkownik ma ograniczoną ilość prób.

# W każdym momencie, zamiast podania litery użytkownik może spróbować odgadnąć całe hasło.
import random

dic_of_words = {
    'owoce': ['brzoskwinia', 'gruszka', 'morela', 'granat'],
    'marki samochodów': ['fiat', 'bmw', 'lamborgini', 'ford'],
    'polskie kluby piłkarskie': ['LECH', 'raków', 'stal']
}

Categories = list(dic_of_words.keys())
select_cat = random.choice(Categories)

if select_cat == 'owoce':
    word = random.choice(dic_of_words['owoce'])
elif select_cat == 'marki samochodów':
    word = random.choice(dic_of_words['marki samochodów'])
else:
    word = random.choice(dic_of_words['polskie kluby piłkarskie'])
szuk_slowo = word.title()
word = list(word.upper())

leng = len(word)
leng_of_word = list(("_" * leng))
print('Kategoria: ', select_cat + "Liczba liter wynosi: ", leng)
proba = 0


while word != leng_of_word:
    print(leng_of_word)
    print()
    litera = input("Podaj literę/słowo: ")
    litera = litera.upper()
    if len(litera) != 1 and (len(litera) < leng) or (len(litera) > leng):
        print("Podaj litere lub słowo!")
        proba += 1
    elif list(litera) == word:
        break
    elif word.count(litera):
        for pos, char in enumerate(word):
            if (char == litera):
                leng_of_word[pos] = word[pos]
    else:
        proba += 1
        if proba == 6:
            print("Przegrałeś!")
            break
        else:
            print("Spróbuj raz jescze!")

print(f'Szukane słowo to "{szuk_slowo}"')