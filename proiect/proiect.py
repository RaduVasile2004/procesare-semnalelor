import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import convolve2d
from skimage import io, color
import os
import matplotlib

matplotlib.use('TkAgg')


def detectie_contururi(image_path, prag=0.2):
    # incarcare
    if not os.path.exists(image_path):
        print(f"Eroare: Nu gasesc fisierul '{image_path}'")
        return

    try:
        img_original = io.imread(image_path)
    except Exception as e:
        print(f"Eroare la citirea imaginii: {e}")
        return

    # conversie alb negru
    if len(img_original.shape) == 3:
        img_gray = color.rgb2gray(img_original)
    else:
        # daca e deja gri ne asiguram ca e float intre 0 si 1(evitam underflow in uint8)(overflow la magnitudine)
        img_gray = img_original / 255.0

    # operatori Sobel
    # Gx linii verticale
    Gx = np.array([[-1, 0, 1],
                   [-2, 0, 2],
                   [-1, 0, 1]])

    # Gy linii orizontale
    Gy = np.array([[1, 2, 1],
                   [0, 0, 0],
                   [-1, -2, -1]])

    # convolutia, filtre
    edges_x = convolve2d(img_gray, Gx, mode='same', boundary='symm')
    edges_y = convolve2d(img_gray, Gy, mode='same', boundary='symm')

    # magnitudinea gradientului
    # sqrt(Gx^2 + Gy^2)
    magnitude = np.sqrt(edges_x ** 2 + edges_y ** 2)

    # normalizare intre 1 si 0
    magnitude = magnitude / np.max(magnitude)

    # thresholding
    # tot ce e sub prag devine negru restul devine alb
    contur_binar = magnitude > prag

    # afisare
    fig, ax = plt.subplots(1, 3, figsize=(15, 6))

    ax[0].imshow(img_gray, cmap='gray')
    ax[0].set_title('Imagine Originala')
    ax[0].axis('off')

    ax[1].imshow(magnitude, cmap='gray')
    ax[1].set_title('Gradient (Matematic)')
    ax[1].axis('off')

    ax[2].imshow(contur_binar, cmap='gray')
    ax[2].set_title(f'Contur Final (Prag > {prag})')
    ax[2].axis('off')

    plt.tight_layout()

    nume_fisier_iesire = 'rezultat_final5.png'
    plt.savefig(nume_fisier_iesire, dpi=300)
    print(f"Succes! Imaginea a fost salvata ca '{nume_fisier_iesire}' in proiectul tau.")

    plt.show()


# prag intre 0,1 0,5 pentru a prinde mai multe sau mai putine detalii
detectie_contururi('img.png', prag=0.5)