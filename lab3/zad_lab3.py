from PIL import Image
import numpy as np


# zad1
# 3.1
def rysuj_ramki_szare(w, h, dzielnik):
    t = (h, w)
    tab = np.zeros(t, dtype=np.uint8)
    grub = int(min(w, h) / dzielnik)
    for i in range(1, int((h / grub))):
        z1 = h - grub * i
        z2 = w - grub * i
        tab[grub * i:z1, grub * i:z2] = 255 - i * grub
    return tab * 255


tab1 = rysuj_ramki_szare(480, 320, 30)
ramki = Image.fromarray(tab1)
ramki.save("obraz1_1.jpg")
ramki.save("obraz1_1.png")


ramki.show()


# 3.4
def rysuj_kratke_szare(w, h, rozmiar):
    t = (h, w)
    tab = np.zeros(t, dtype=np.uint8)
    for x in range(w):
        for y in range(h):
            if (x % rozmiar) // (rozmiar / 2) == (y % rozmiar) // (rozmiar / 2):
                tab[y, x] = 100
            else:
                tab[y, x] = 200
    return tab


tab2 = rysuj_kratke_szare(500, 500, 50)
kratka = Image.fromarray(tab2)
kratka.save("obraz1_2.jpg")
kratka.save("obraz1_2.png")


kratka.show()


# zad2
# 3.2
def rysuj_pasy_pionowe_kolorowe(w, h, dzielnik):
    t = (h, w, 3)
    tab = np.ones(t, dtype=np.uint8)
    grub = int(w / dzielnik)
    for k in range(dzielnik):
        for g in range(grub):
            i = k * grub + g
            for j in range(h):
                if k % 3 == 0:
                    tab[j, i] = [255, 0, 0]
                elif k % 3 == 1:
                    tab[j, i] = [0, 255, 0]
                else:
                    tab[j, i] = [0, 0, 255]
    return tab


tab3 = rysuj_pasy_pionowe_kolorowe(480, 320, 8)
pasy_poziome = Image.fromarray(tab3)
pasy_poziome.show()
pasy_poziome.save("obraz2.jpg")
pasy_poziome.save("obraz2.png")


# zad3
def koloruj_obraz(obraz, dzielnik):
    t_obraz = np.asarray(obraz)
    h, w = t_obraz.shape
    t = (h, w, 3)
    tab = np.zeros(t, dtype=np.uint8)
    grub = int(h / dzielnik)
    for k in range(dzielnik):
        for g in range(grub):
            i = k * grub + g
            for j in range(w):
                if not t_obraz[i, j]:
                    if k % 3 == 0:
                        tab[i, j] = [255, 0, 0]
                    elif k % 3 == 1:
                        tab[i, j] = [0, 255, 0]
                    else:
                        tab[i, j] = [0, 0, 255]
                else:
                    tab[i, j] = [255, 255, 255]
    return tab


inicjaly = Image.open("inicjaly.bmp")
kolorowe_inicjaly = Image.fromarray(koloruj_obraz(inicjaly, 10))
kolorowe_inicjaly.show()
kolorowe_inicjaly.save("obraz3.png")
kolorowe_inicjaly.save("obraz3.jpg")


def negatyw_szare(tab):
    h, w = tab.shape
    tab_neg = tab.copy()
    for i in range(h):
        for j in range(w):
            tab_neg[i, j] = 255 - tab[i, j]
    return tab_neg


ramki_negatyw = Image.fromarray(negatyw_szare(tab1))
ramki_negatyw.save("obraz1_1N.jpg")
ramki_negatyw.save("obraz1_1N.png")
# ramki_negatyw.show()

kratka_negatyw = Image.fromarray(negatyw_szare(tab2))
kratka_negatyw.save("obraz1_2N.jpg")
kratka_negatyw.save("obraz1_2N.png")


kratka_negatyw.show()


def negatyw_rgb(tab):
    negatyw = 255 - tab
    return negatyw


pasy_poziome_negatyw = Image.fromarray(negatyw_rgb(tab3))
pasy_poziome_negatyw.save("obraz2N.jpg")
pasy_poziome_negatyw.save("obraz2N.png")
pasy_poziome_negatyw.show()
