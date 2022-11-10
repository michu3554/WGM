from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

im = Image.open("obraz.jpg")
inicjaly = Image.open("inicjaly.bmp")

def zakres(w, h):  # funkcja, która uprości podwójna petle for
    return [(i, j) for i in range(w) for j in range(h)]

def wstaw_inicjaly(obraz, inicjaly, m, n, kolor):
    obraz1 = obraz.copy()
    w, h = obraz.size
    w0, h0 = inicjaly.size
    for i, j in zakres(w0, h0):
        if i + m < w and j + n < h:
            if inicjaly.getpixel((i, j )) == 0:
                obraz1.putpixel((i + m, j + n), (kolor))
            else:
                obraz1.putpixel((i + m, j + n), (255,255,255))
    return obraz1

# obraz1 = wstaw_inicjaly(im, inicjaly, 1440, 1998, (255, 0, 0))
# obraz1.show()
# obraz1.save("obraz1.png")

def wstaw_inicjaly_maska(obraz, inicjaly, m, n, x, y, z):
    obraz1 = obraz.copy()
    w, h = obraz.size
    w0, h0 = inicjaly.size
    for i, j in zakres(w0, h0):
        if i + m < w and j + n < h:
            if inicjaly.getpixel((i, j)) == 0:
                p = obraz.getpixel((i + m, j + n))
                obraz1.putpixel((i + m, j + n), (p[0] + x, p[1] + y, p[2] + z))
    return obraz1

# obraz2 = wstaw_inicjaly_maska(im, inicjaly, 770, 974, -255, 255, -255)
# obraz2.show()
# obraz2.save("obraz1.png")

def wstaw_inicjaly_load(obraz, inicjaly, m, n, kolor):
    pix = obraz.load()
    pix2 = inicjaly.load()
    w, h, = obraz.size
    w0, h0, = inicjaly.size
    for i, j in zakres(w0, h0):
        if i + m < w and j + n < h:
            if pix2[i, j] == 0:
                pix[i + m, j + n] = (kolor)
            else:
                pix[i + m, j+ n] = (255, 255, 255)
    return obraz

# test = wstaw_inicjaly_load(im, inicjaly, 1440, 1998, (255, 0, 0))
# test.show()

def wstaw_inicjaly_maska_load(obraz, inicjaly, m, n, x, y, z):
    pix = obraz.load()
    pix2 = inicjaly.load()
    w, h = obraz.size
    w0, h0 = inicjaly.size
    for i, j in zakres(w0, h0):
        if i + m < w and j + n < h:
            if pix2[i, j] == 0:
                pix[i + m, j + n] = (x, y, z)
    return obraz

# test = wstaw_inicjaly_maska_load(im, inicjaly, 770, 974, -255, 255, -255)
# test.show()

def kontrast(obraz, wsp_kontrastu):
    mn = ((255 + wsp_kontrastu) / 255) ** 2
    if (wsp_kontrastu >=0  <= 100):
        return obraz.point(lambda i: 128 + (i - 128) * mn)

# test = kontrast(im, 0)
# test.show()

def transformacja_logarytmiczna(obraz):
    return obraz.point(lambda i: 255 * np.log(1 + i / 255))

# test = transformacja_logarytmiczna(im)
# test.show()

def transformacja_gamma(obraz, gamma):
    if gamma > 0:
        return obraz.point(lambda i: (i / 255) ** (1 / gamma) * 255)

# test = transformacja_gamma(im, 150)
#  test.show()