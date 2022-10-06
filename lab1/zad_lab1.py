from PIL import Image
import numpy as np

# zad2
obraz = Image.open("inicjaly.bmp")
obraz.show()

print("tryb:", obraz.mode)
print("format:", obraz.format)
print("rozmiar:", obraz.size, "\n")

# zad3
dane_obraz = np.asarray(obraz)
dane_obraz1 = dane_obraz * 1

tablica = open('inicjaly.txt', 'w')
for rows in dane_obraz1:
    for item in rows:
        tablica.write(str(item) + ' ')
    tablica.write('\n')

# zad4
print("typ danych tablicy:", dane_obraz.dtype)
print("rozmiar tablicy:", dane_obraz.shape)
print("liczba elementów:", dane_obraz.size)
print("wymiar tablicy:", dane_obraz.ndim)
print("rozmiar wyrazu tablicy:", dane_obraz.itemsize, "\n")

print("Wartosc piksela z adresu (50,30):", dane_obraz[30][50])
print("Wartosc piksela z adresu (90,40):", dane_obraz[40][90])
print("Wartosc piksela z adresu (99,0):", dane_obraz[0][99], "\n")

# zad5
tablica.close()
t1 = np.loadtxt("inicjaly.txt", dtype=np.bool_)
porownanie = t1 == dane_obraz
czy_rowne = porownanie.all()
print("Czy sa rowne?",czy_rowne)
print("typ danych tablicy:", t1.dtype)
print("rozmiar tablicy:", t1.shape)
print("liczba elementów:", t1.size)
print("wymiar tablicy:", t1.ndim)
print("rozmiar wyrazu tablicy:", t1.itemsize, "\n")

# zad6
t2 = np.loadtxt("inicjaly.txt", dtype=np.int_)
porownanie2 = t2 == dane_obraz
czy_rowne2 = porownanie2.all()
print("Czy sa rowne?", czy_rowne2)
print("typ danych tablicy:", t2.dtype)
print("rozmiar tablicy:", t2.shape)
print("liczba elementów:", t2.size)
print("wymiar tablicy:", t2.ndim)
print("rozmiar wyrazu tablicy:", t2.itemsize, "\n")

obraz1 = Image.fromarray(t2)
obraz1.show()
