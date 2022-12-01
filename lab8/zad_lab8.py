from PIL import Image
from PIL import ImageChops, ImageOps, ImageFilter
from PIL import ImageStat as stat
import matplotlib.pyplot as plt


def statystyki(im):
    s = stat.Stat(im)
    print("extrema: ", s.extrema)
    print("count: ", s.count)
    print("mean: ", s.mean)
    print("median: ", s.median)
    print("stddev: ", s.stddev)


im = Image.open('obraz.jpg')
print("Tryb obrazu: ", im.mode)
obraz = im.convert("L")
statystyki(obraz)
print(obraz.histogram())

hist = obraz.histogram()
plt.title("histogram - teeth")
plt.bar(range(256), hist[0:256], color='b', alpha=0.8)
plt.show()


def histogram_norm(obraz):
    w, h = obraz.size
    n = w * h
    hist = obraz.histogram()
    hist_norm = [x / n for x in hist]
    return hist_norm


hist1 = histogram_norm(obraz)
plt.title("histogram - teeth")
plt.plot(range(256), hist1[0:256], color='b', alpha=0.8)
plt.show()


def histogram_cumul(obraz):
    hist_norm = histogram_norm(obraz)
    hist_cumul = []
    suma = 0
    for i in range(0, 256, 1):
        suma += hist_norm[i]
        hist_cumul.append(suma)
    return hist_cumul


hist2 = histogram_cumul(obraz)
plt.title("histogram - teeth")
plt.plot(range(256), hist2[0:256], color='b', alpha=0.8)
plt.show()


def histogram_equalization(obraz):
    obraz1 = obraz.copy()
    hist_cumul = histogram_cumul(obraz1)
    w, h = obraz.size
    for i in range(w):
        for j in range(h):
            p = obraz1.getpixel((i, j))
            obraz1.putpixel((i, j), int(255 * hist_cumul[p]))
    return obraz1


equalized = histogram_equalization(obraz)
equalized.save("equalized.png")

equalized.show()

equalized1 = ImageOps.equalize(obraz)
equalized1.save("equalized1.png")
equalized1.show()

diff = ImageChops.difference(equalized, equalized1)
diff.show()

hist_eq = equalized.histogram()
hist_eq1 = equalized1.histogram()
plt.title("histogram - porownanie")
plt.bar(range(256), hist_eq[:256], color='r', alpha=0.8)
plt.bar(range(256), hist_eq1[:256], color='g', alpha=0.8)
plt.show()

statystyki(equalized)
statystyki(equalized1)

detail = obraz.filter(ImageFilter.DETAIL)
sharpen = obraz.filter(ImageFilter.SHARPEN)
contour = obraz.filter(ImageFilter.CONTOUR)

plt.figure(figsize=(36, 12))
plt.subplot(1, 4, 1)
plt.title("EQUALIZE")
plt.axis('off')
plt.imshow(equalized1, "gray")
plt.subplot(1, 4, 2)
plt.title("DETAIL")
plt.axis('off')
plt.imshow(detail, "gray")
plt.subplot(1, 4, 3)
plt.title("SHARPEN")
plt.axis('off')
plt.imshow(sharpen, "gray")
plt.subplot(1, 4, 4)
plt.title("CONTOUR")
plt.axis('off')
plt.imshow(contour, "gray")
plt.savefig("filtry.png")
plt.show()
