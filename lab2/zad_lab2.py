from PIL import Image
import numpy as np


def wstaw_obraz(obraz_wstawiany, w_m, h_m, wsp):
    h0, w0 = obraz_wstawiany.shape
    t = (int(wsp * h0), int(wsp * w0))
    tab = np.zeros(t, dtype=np.uint8)
    for i in range(h_m, h_m + h0):
        for j in range(w_m, w_m + w0):
            if i < (wsp * h0) and j < (wsp * w0):
                tab[i][j] = obraz_wstawiany[i - h_m][j - w_m]
    tab = tab.astype(bool)
    po_wstawieniu = Image.fromarray(tab)
    return po_wstawieniu


inicjaly = Image.open("inicjaly.bmp")
t_inicjaly = np.asarray(inicjaly)
po_wstawieniu = wstaw_obraz(t_inicjaly, 125, 75, 2)
po_wstawieniu2 = wstaw_obraz(t_inicjaly, 300, 150, 10)
po_wstawieniu3 = wstaw_obraz(t_inicjaly, 0, 0, 3)
po_wstawieniu.save("po_wstawieniu1.bmp")
po_wstawieniu2.save("po_wstawieniu2.bmp")
po_wstawieniu3.save("po_wstawieniu3.bmp")
po_wstawieniu.show()
po_wstawieniu2.show()
po_wstawieniu3.show()


def rysuj_ramke(w, h, dzielnik):
    t = (h, w)
    tab = np.zeros(t, dtype=np.uint8)
    grub = int(min(w, h) / dzielnik)
    for i in range(1, int((h / grub))):
        z1 = h - grub * i
        z2 = w - grub * i
        if i % 2 != 0:
            tab[grub * i:z1, grub * i:z2] = 1
        else:
            tab[grub * i:z1, grub * i:z2] = 0
    return tab * 255


tab = rysuj_ramke(480, 320, 16)
im_ramka = Image.fromarray(tab)
im_ramka.save("rysuj_ramke.bmp")
im_ramka.show()


def rysuj_pasy_pionowe(w, h, dzielnik):
    t = (h, w)
    tab = np.ones(t, dtype=np.uint8)
    grub = int(w / dzielnik)
    for k in range(dzielnik):
        for g in range(grub):
            i = k * grub + g
            for j in range(h):
                tab[j, i] = k % 2
    tab = tab * 255
    obraz = Image.fromarray(tab)
    obraz.save("rysuj_pasy_pionowe.bmp")
    obraz.show()


rysuj_pasy_pionowe(480, 320, 8)


def rysuj_prostokaty(w, h, m, n):
    t = (h, w)
    tab = np.ones(t, dtype=np.uint8)
    tab[n:h, m:w] = 0
    tab[0:n, 0:m] = 0
    tab = tab * 255
    obraz = Image.fromarray(tab)
    obraz.save("rysuj_prostokaty.bmp")
    obraz.show()


rysuj_prostokaty(480, 320, 100, 50)


def rysuj_kratke(w, h, rozmiar):
    t = (h, w)
    tab = np.zeros(t, dtype=np.uint8)
    for x in range(w):
        for y in range(h):
            if (x % rozmiar) // (rozmiar / 2) == (y % rozmiar) // (rozmiar / 2):
                tab[y, x] = 0
            else:
                tab[y, x] = 255
    obraz = Image.fromarray(tab)
    obraz.save("rysuj_kratke.bmp")
    obraz.show()


rysuj_kratke(500, 500, 50)
