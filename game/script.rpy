# The script of the game goes in this file.






# The game starts here.
label start:
    #Logo gry, intro, muzyka startowa, menu główne
    #
    #
    #
    show bg room
    "Intro"
    jump prologStart
#prolog zaczyna się tutaj
label prologStart:
    #Wprowadzenie fabularne
    "Prolog"
    #Przedstawienie postaci(wstępne)
    #
    #
    jump akt_1_start
# Akt 1 zaczyna się tutaj
label akt_1_start:
    "Akt I"
    #ruiny, 1-2 sceny przed rozdrożem, 
    #rozdroże i 3 opcje przejścia konczące w tym samym miejscu, bez możliwośći powrotu(wrota sie zamykają, nie można zmienić ścieżki)
    #
    #scena końcowa z uwięzionymi zakończenie aktu1
    #
    #
    jump akt_2_Start
# Akt 2 zaczyna się tutaj
label akt_2_Start:
    "Akt II"
    #Miasto
    #Mapa interaktywna(scene)
    #
    #
    jump outro
#Outro zaczyna sie tutaj
label outro:
    "Outro"
    #
    #
    #
    #
    jump endgame
# This ends the game.
label endgame:
    "Koniec gry"
    # This ends the game.

    return
