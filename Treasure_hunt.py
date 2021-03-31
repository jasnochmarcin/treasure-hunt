from random import randint
pozycjax = randint(1 , 10)
pozycjay = randint(1 , 10)
skarbx = randint(1 , 10)
skarby = randint(1 , 10)
ruchy = 0
print('Witaj w grze "Poszukiwanie skarbu", możesz poruszać się w czterech kierunkach wpisująć "lewo", "prawo", "góra" lub "dół", tak długo, aż znajdziesz skarb')
print('Uwaga po przekroczeniu 30 kroków, skarb zmieni swoje położenie')
print("Ktoś będzie Ci podpowiadał czy idziesz w dobrym kierunku, jednak może się zdarzyć, że nie dostaniesz podpowiedzi. Powodzenia!")

while True:
    if pozycjax == skarbx and pozycjay == skarby:
        print('Gratulacje, znalazłeś skarb!')
        print('Liczba ruchów które wykonałeś to: ', ruchy)
        break
    elif pozycjax != skarbx and pozycjay != skarby or pozycjax == skarbx and pozycjay != skarby or pozycjax != skarbx and pozycjay == skarby:
        odleglosc_przed = abs(pozycjax - skarbx) + abs(pozycjay - skarby)
        #print('Pozycja skarbu to: x=', skarbx , 'y=' , skarby)
        kierunek = input('Wybierz kierunek i wciśnij "enter"')
        if kierunek == "lewo":
            pozycjax -= 1
            ruchy += 1
            print("x=" , pozycjax , "y=" , pozycjay)
            if pozycjax > 10 or pozycjax <= 0 or pozycjay > 10 or pozycjay <= 0:
                print('Wyszedłeś poza planszę, koniec gry.')
                break
        elif kierunek == "prawo":
            pozycjax += 1
            ruchy += 1
            print("x=", pozycjax, "y=", pozycjay)
            if pozycjax > 10 or pozycjax <= 0 or pozycjay > 10 or pozycjay <= 0:
                print('Wyszedłeś poza planszę, koniec gry.')
                break
        elif kierunek == "góra":
            pozycjay += 1
            ruchy += 1
            print("x=", pozycjax, "y=", pozycjay)
            if pozycjax > 10 or pozycjax <= 0 or pozycjay > 10 or pozycjay <= 0:
                print('Wyszedłeś poza planszę, koniec gry.')
                break
        elif kierunek == "dół":
            pozycjay -= 1
            ruchy += 1
            print("x=", pozycjax, "y=", pozycjay)
            if pozycjax > 10 or pozycjax <= 0 or pozycjay > 10 or pozycjay <= 0:
                print('Wyszedłeś poza planszę, koniec gry.')
                break
        else:
            print('Podałeś niepoprawny kierunek')

        odleglosc_po = abs(pozycjax - skarbx) + abs(pozycjay - skarby)
        bezpodpowiedzi = randint(1 , 5)
        if bezpodpowiedzi == 1:
            print("Tym razem nie dostaniesz podpowiedzi")
        elif odleglosc_po < odleglosc_przed:
            print('Ciepło')
        else:
            print('Zimno')

        if ruchy > 30:
            skarbx = randint(1, 10)
            skarby = randint(1, 10)
            ruchy = 0

    else:
        print('Spróbuj jeszcze raz')
        continue