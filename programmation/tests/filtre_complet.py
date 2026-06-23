import matplotlib.pyplot as plt

Mat = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 102, 255, 102, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 51, 204, 255, 102, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 102, 255, 255, 51, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 51, 204, 255, 204, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 102, 255, 255, 153, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 153, 255, 204, 51, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 51, 204, 255, 204, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 102, 255, 255, 153, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 153, 255, 255, 102, 0, 0, 0, 0, 0, 0, 51, 153, 51, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 204, 255, 204, 51, 0, 0, 0, 0, 0, 0, 102, 255, 102, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 51, 255, 255, 153, 0, 0, 0, 0, 0, 0, 0, 153, 255, 153, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 102, 255, 255, 51, 0, 0, 0, 0, 0, 0, 0, 204, 255, 204, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 153, 255, 204, 51, 51, 51, 51, 51, 51, 51, 102, 255, 255, 255, 153, 102, 51, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 204, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 204, 51, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 102, 153, 204, 204, 204, 204, 204, 204, 204, 204, 204, 255, 255, 255, 204, 153, 102, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 153, 255, 204, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 153, 255, 204, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 153, 255, 204, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 153, 255, 204, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 102, 204, 153, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

flt_hori = [[1,2,1],
            [0,0,0],
            [-1,-2,-1]]

def new_mat(n):
    return [[0 for _ in range(n)] for _ in range(n)]


def calcul(mat,filtre):
    n = len(mat) - len(filtre) + 1
    sol = new_mat(n)
    for i in range(n):
        for j in range(n):
            somme = 0
            for k in range(len(filtre)):
                for l in range(len(filtre)):
                    somme += mat[i+k][j+l]*filtre[k][l]
            sol[i][j] = somme
    return sol


def MaxPool(mat):
    n = len(mat)
    # Formule officielle : ((Entree - Filtre) // Pas) + 1
    # Pour n=5 : ((5 - 2) // 2) + 1 = 1 + 1 = 2. On ignore le bord.
    taille_sortie = ((n - 2) // 2) + 1
    res = new_mat(taille_sortie)
    
    # On s'arrête à n - 1 pour éviter que i + 1 ou j + 1 ne déborde
    for i in range(0, n - 1, 2):
        for j in range(0, n - 1, 2):
            val = []
            for k in range(2):
                for l in range(2):
                    val.append(mat[i + k][j + l])
            val_max = max(val)
            res[i // 2][j // 2] = val_max
    return res

# Ligne 1 : Opérations sur l'image originale 28x28
res_hori = calcul(Mat, flt_hori)    # Sortie : 26x26
mp_hori = MaxPool(Mat)              # Sortie : 14x14
mp_bis_hori = MaxPool(res_hori)     # Sortie : 13x13 (car 26//2 = 13)

# Ligne 2 : Seconde couche de traitement (on applique la suite sur mp_bis_hori)
mp_hori2 = calcul(mp_bis_hori, flt_hori) # Sortie : 13 - 3 + 1 = 11x11
mp_bis_hori2 = MaxPool(mp_hori2)

fig, axes = plt.subplots(2, 3, figsize=(16, 8))

# Ligne du haut
axes[0, 0].imshow(Mat, cmap='gray', interpolation='nearest')
axes[0, 0].set_title("Original (28x28)")
axes[0, 0].axis('off')

axes[0, 1].imshow(res_hori, cmap='gray', interpolation='nearest')
axes[0, 1].set_title("Filtre horizontal (26x26)")
axes[0, 1].axis('off')

axes[0, 2].imshow(mp_hori, cmap='gray', interpolation='nearest')
axes[0, 2].set_title("MP Original seul (14x14)")
axes[0, 2].axis('off')

# Ligne du bas
axes[1, 0].imshow(mp_bis_hori, cmap='gray', interpolation='nearest')
axes[1, 0].set_title("Filtre Horizontal + MP (13x13)")
axes[1, 0].axis('off')

axes[1, 1].imshow(mp_hori2, cmap='gray', interpolation='nearest')
axes[1, 1].set_title("Deuxième Filtre Horiz. (11x11)")
axes[1, 1].axis('off')

axes[1, 2].imshow(mp_bis_hori2, cmap='gray', interpolation='nearest')
axes[1, 2].set_title("Deuxième MP (5x5)")
axes[1, 2].axis('off')

plt.tight_layout()
plt.show()