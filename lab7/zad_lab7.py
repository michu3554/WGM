from PIL import Image
from PIL import ImageFilter
from PIL import ImageChops
import matplotlib.pyplot as plt
import numpy as np

obraz = Image.open("obraz.jpg")


# Zadanie 1
def filtruj(obraz, kernel, scale):
    obraz1 = obraz.copy()
    obraz_pix = obraz.load()
    obraz1_pix = obraz1.load()
    w, h = obraz.size
    m = len(kernel)
    d = int(m / 2)
    for i in range(d, w - d):
        for j in range(d, h - d):
            temp = [0, 0, 0]
            for k in range(m):
                for l in range(m):
                    i_n = i + k - d
                    j_n = j + l - d
                    pixel = obraz_pix[i_n, j_n]
                    temp[0] += pixel[0] * kernel[k][l]
                    temp[1] += pixel[1] * kernel[k][l]
                    temp[2] += pixel[2] * kernel[k][l]
                obraz1_pix[i, j] = (int(temp[0] / scale), int(temp[1] / scale), int(temp[2] / scale))
    return obraz1


blur_para = ImageFilter.BLUR.filterargs
print(blur_para)
t = [[1, 1, 1, 1, 1], [1, 0, 0, 0, 1], [1, 0, 0, 0, 1], [1, 0, 0, 0, 1], [1, 1, 1, 1, 1]]
scale = np.sum(t)
blur1 = filtruj(obraz, t, scale)
blur = obraz.filter(ImageFilter.BLUR)
porownanie_blur = ImageChops.difference(blur, blur1)

plt.figure(figsize=(32, 8))
plt.subplot(1, 3, 1)
plt.title("blur")
plt.axis('off')
plt.imshow(blur)
plt.subplot(1, 3, 2)
plt.title("blur1")
plt.axis('off')
plt.imshow(blur1)
plt.subplot(1, 3, 3)
plt.title("porownanie")
plt.axis('off')
plt.imshow(porownanie_blur)
plt.subplots_adjust(wspace=0.05)
plt.savefig('fig1.png')

obraz_L = obraz.convert('L')
x = ImageFilter.EMBOSS.filterargs

ImageFilter.EMBOSS.filterargs = ((3, 3), 1, 128, (-1, 0, 1, -2, 0, 2, -1, 0, 1))
sobel1 = obraz_L.filter(ImageFilter.EMBOSS)

ImageFilter.EMBOSS.filterargs = ((3, 3), 1, 128, (-1, -2, -1, 0, 0, 0, 1, 2, 1))
sobel2 = obraz_L.filter(ImageFilter.EMBOSS)

plt.figure(figsize=(32, 8))
plt.subplot(1, 3, 1)
plt.title("Obraz w trybie L")
plt.axis('off')
plt.imshow(obraz_L, "gray")
plt.subplot(1, 3, 2)
plt.title("SOBEL1")
plt.axis('off')
plt.imshow(sobel1, "gray")
plt.subplot(1, 3, 3)
plt.title("SOBEL2")
plt.axis('off')
plt.imshow(sobel2, "gray")
plt.subplots_adjust(wspace=0.05)
plt.savefig('fig2.png')

# Zadanie 4
filtr2 = obraz.filter(ImageFilter.DETAIL)
filtr4 = obraz.filter(ImageFilter.EDGE_ENHANCE_MORE)
filtr6 = obraz.filter(ImageFilter.SHARPEN)
filtr8 = obraz.filter(ImageFilter.SMOOTH_MORE)
porownanie2 = ImageChops.difference(filtr2, obraz)
porownanie4 = ImageChops.difference(filtr4, obraz)
porownanie6 = ImageChops.difference(filtr6, obraz)
porownanie8 = ImageChops.difference(filtr8, obraz)

plt.figure(figsize=(16, 32))
plt.subplot(4, 2, 1)
plt.title("DETAIL")
plt.imshow(filtr2)
plt.axis("off")
plt.subplot(4, 2, 2)
plt.title("DETAIL POROWNANIE")
plt.imshow(porownanie2)
plt.axis("off")
plt.subplot(4, 2, 3)
plt.title("EDGE_ENHANCE_MORE")
plt.imshow(filtr4)
plt.axis("off")
plt.subplot(4, 2, 4)
plt.title("EDGE_ENHANCE_MORE POROWNANIE")
plt.imshow(porownanie4)
plt.axis("off")
plt.subplot(4, 2, 5)
plt.title("SHARPEN")
plt.imshow(filtr6)
plt.axis("off")
plt.subplot(4, 2, 6)
plt.title("SHARPEN POROWNANIE")
plt.imshow(porownanie6)
plt.axis("off")
plt.subplot(4, 2, 7)
plt.title("SMOOTH_MORE")
plt.imshow(filtr8)
plt.axis("off")
plt.subplot(4, 2, 8)
plt.title("SMOOTH_MORE POROWNANIE")
plt.imshow(porownanie8)
plt.axis("off")
plt.subplots_adjust(wspace=0.05, hspace=0.2)
plt.savefig("fig3.png")

# podpunkt b
filtr12 = obraz.filter(ImageFilter.GaussianBlur(radius=2))
filtr13 = obraz.filter(ImageFilter.UnsharpMask(radius=2, percent=150, threshold=3))
filtr16 = obraz.filter(ImageFilter.MedianFilter(size=5))
filtr17 = obraz.filter(ImageFilter.MinFilter(size=5))
filtr18 = obraz.filter(ImageFilter.MaxFilter(size=5))
porownanie12 = ImageChops.difference(filtr12, obraz)
porownanie13 = ImageChops.difference(filtr13, obraz)
porownanie16 = ImageChops.difference(filtr16, obraz)
porownanie17 = ImageChops.difference(filtr17, obraz)
porownanie18 = ImageChops.difference(filtr18, obraz)

plt.figure(figsize=(16, 32))
plt.subplot(5, 2, 1)
plt.title("GaussianBlur, radius = 2")
plt.imshow(filtr12)
plt.axis("off")
plt.subplot(5, 2, 2)
plt.title("GaussianBlur porownanie")
plt.imshow(porownanie12)
plt.axis("off")
plt.subplot(5, 2, 3)
plt.title("UnsharpMask, radius = 2, percent = 150, threshold = 3")
plt.imshow(filtr13)
plt.axis("off")
plt.subplot(5, 2, 4)
plt.title("UnsharpMask porownanie")
plt.imshow(porownanie13)
plt.axis("off")
plt.subplot(5, 2, 5)
plt.title("MedianFilter, size  5")
plt.imshow(filtr16)
plt.axis("off")
plt.subplot(5, 2, 6)
plt.title("MedianFilter porownanie")
plt.imshow(porownanie16)
plt.axis("off")
plt.subplot(5, 2, 7)
plt.title("MinFilter, size =5 ")
plt.imshow(filtr17)
plt.axis("off")
plt.subplot(5, 2, 8)
plt.title("MinFilter porownanie")
plt.imshow(porownanie17)
plt.axis("off")
plt.subplot(5, 2, 9)
plt.title("MaxFilter, size = 5")
plt.imshow(filtr18)
plt.axis("off")
plt.subplot(5, 2, 10)
plt.title("MaxFilter porownanie")
plt.imshow(porownanie18)
plt.axis("off")
plt.subplots_adjust(wspace=0.05, hspace=0.2)
plt.savefig("fig4.png")
