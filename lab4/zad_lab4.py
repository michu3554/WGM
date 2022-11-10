from PIL import Image
import numpy as np
from PIL import ImageChops
import matplotlib.pyplot as plt

# Zad1
im1 = Image.open("obraz.jpg")

# Zad2
T1 = np.asarray(im1)
t_r = T1[:, :, 0]
t_g = T1[:, :, 1]
t_b = T1[:, :, 2]
im_r = Image.fromarray(t_r)
im_g = Image.fromarray(t_g)
im_b = Image.fromarray(t_b)

im2 = Image.merge('RGB', (im_r, im_g, im_b))
diff = ImageChops.difference(im1, im2)
T2 = np.asarray(im2)

im1.show()
im2.show()
diff.show()
print((T1 == T2).all())

# Zad3
r, g, b = im1.split()
im3 = Image.merge('RGB', (r, b, g))

im3.save("im3.jpg")
im3.save("im3.png")

im3_jpg = Image.open("im3.jpg")
im3_png = Image.open("im3.png")
diff2 = ImageChops.difference(im3_jpg, im3_png)
diff2.show()

obraz1_1_jpg = Image.open('obraz1_1.png')
obraz1_1_png = Image.open('obraz1_1.jpg')
obraz1_1N_jpg = Image.open('obraz1_1N.jpg')
obraz1_1N_png = Image.open('obraz1_1N.png')
obraz1_2_jpg = Image.open('obraz1_2.jpg')
obraz1_2_png = Image.open('obraz1_2.png')
obraz1_2N_jpg = Image.open('obraz1_2N.jpg')
obraz1_2N_png = Image.open('obraz1_2N.png')
diff01 = ImageChops.difference(obraz1_1_jpg, obraz1_1_png)
diff02 = ImageChops.difference(obraz1_1N_jpg, obraz1_1N_png)
diff03 = ImageChops.difference(obraz1_2_jpg, obraz1_2_png)
diff04 = ImageChops.difference(obraz1_2N_jpg, obraz1_2N_png)
plt.figure(figsize=(32, 16))
plt.subplot(2, 2, 1)
plt.imshow(diff01, "gray")
plt.axis('off')
plt.subplot(2, 2, 2)
plt.imshow(diff02, "gray")
plt.axis('off')
plt.subplot(2, 2, 3)
plt.imshow(diff03, "gray")
plt.axis('off')
plt.subplot(2, 2, 4)
plt.imshow(diff04, "gray")
plt.axis('off')
plt.subplots_adjust(wspace=0.05, hspace=0.05)
plt.savefig('fig1.png')


# plt.show()

# Zad4
def szarosci(obraz):
    szare = obraz.convert("L")
    t = np.asarray(szare)
    return t


tab = szarosci(im1)
im4 = Image.fromarray(tab)

obraz01 = Image.merge('RGB', (im4, g, b))
obraz02 = Image.merge('RGB', (r, im4, b))
obraz03 = Image.merge('RGB', (r, g, im4))

plt.figure(figsize=(32, 16))
plt.subplot(1, 3, 1)
plt.imshow(obraz01)
plt.axis('off')
plt.subplot(1, 3, 2)
plt.imshow(obraz02)
plt.axis('off')
plt.subplot(1, 3, 3)
plt.imshow(obraz03)
plt.axis('off')
plt.subplots_adjust(wspace=0.05, hspace=0.05)
plt.savefig('fig2.png')


# plt.show()

# Zad5
def create_obraz(x1, x2, y1, y2):
    tab = np.zeros((300, 300), dtype=np.uint8)

    for i in range(x1, x2):
        for j in range(y1, y2):
            tab[i, j] = 255

    img = Image.fromarray(tab)
    return img


img1 = create_obraz(75, 225, 75, 225)
img2 = create_obraz(0, 300, 125, 175)
img3 = create_obraz(125, 175, 0, 300)

image1 = Image.merge('RGB', (img1, img2, img3))
image2 = Image.merge('RGB', (img1, img3, img2))
image3 = Image.merge('RGB', (img2, img1, img3))
image4 = Image.merge('RGB', (img2, img3, img1))
image5 = Image.merge('RGB', (img3, img1, img2))
image6 = Image.merge('RGB', (img3, img2, img1))

plt.figure(figsize=(32, 16))
plt.subplot(3, 2, 1)
plt.imshow(image1)
plt.axis('off')
plt.subplot(3, 2, 2)
plt.imshow(image2)
plt.axis('off')
plt.subplot(3, 2, 3)
plt.imshow(image3)
plt.axis('off')
plt.subplot(3, 2, 4)
plt.imshow(image4)
plt.axis('off')
plt.subplot(3, 2, 5)
plt.imshow(image5)
plt.axis('off')
plt.subplot(3, 2, 6)
plt.imshow(image6)
plt.axis('off')
plt.subplots_adjust(wspace=0.05, hspace=0.05)
plt.savefig('fig3.png')
plt.show()
