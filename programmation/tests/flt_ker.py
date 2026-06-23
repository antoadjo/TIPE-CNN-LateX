import matplotlib.pyplot as plt

flt_vert = [[1,0,-1],
            [2,0,-2],
            [1,0,-1]]

flt_hori = [[1,2,1],
            [0,0,0],
            [-1,-2,-1]]

flt_diago_des = [[2,1,0],
                 [1,0,-1],
                 [0,-1,-2]]

flt_diago_mon = [[0,1,2],
                 [-1,0,1],
                 [-2,-1,0]]

flt_laplacien = [
    [1, 1, 1],
    [1, -8, 1],
    [1, 1, 1]]

Mat = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 102, 153, 204, 204, 204, 153, 102, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 51, 204, 255, 255, 255, 255, 255, 255, 255, 204, 51, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 102, 255, 255, 204, 102, 51, 0, 51, 102, 204, 255, 255, 102, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 51, 204, 255, 153, 0, 0, 0, 0, 0, 0, 0, 102, 255, 204, 51, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 102, 255, 204, 0, 0, 0, 0, 0, 0, 0, 0, 0, 153, 255, 102, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 153, 255, 102, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 204, 255, 51, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 204, 255, 102, 153, 204, 204, 204, 153, 102, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 204, 255, 255, 255, 255, 255, 255, 255, 255, 255, 204, 102, 51, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 153, 255, 255, 204, 153, 102, 51, 51, 102, 204, 255, 255, 204, 51, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 102, 255, 255, 102, 0, 0, 0, 0, 0, 0, 51, 204, 255, 204, 51, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 51, 204, 255, 153, 0, 0, 0, 0, 0, 0, 0, 51, 204, 255, 153, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 153, 255, 204, 51, 0, 0, 0, 0, 0, 0, 0, 102, 255, 204, 51, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 102, 255, 255, 102, 0, 0, 0, 0, 0, 0, 0, 102, 255, 255, 102, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 51, 204, 255, 204, 51, 0, 0, 0, 0, 0, 51, 204, 255, 204, 51, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 102, 255, 255, 153, 0, 0, 0, 0, 0, 153, 255, 255, 102, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 51, 204, 255, 255, 204, 102, 51, 102, 204, 255, 255, 204, 51, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 102, 255, 255, 255, 255, 255, 255, 255, 255, 204, 102, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 102, 153, 204, 204, 204, 204, 204, 153, 102, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

def afficher_matrice(matrice):
    largeur_max = max(len(str(element)) for ligne in matrice for element in ligne)
    print("[")
    for ligne in matrice:
        ligne_formatee = " ".join(f"{elem:>{largeur_max}}" for elem in ligne)
        print(f"  [ {ligne_formatee} ]")
    print("]")

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

res_vert = calcul(Mat, flt_vert)
res_hori = calcul(Mat, flt_hori)
res_diago_d = calcul(Mat, flt_diago_des)
res_diago_m = calcul(Mat, flt_diago_mon)
res_flou = calcul(Mat, flt_laplacien)

fig, axes = plt.subplots(2, 3, figsize=(10, 5))

axes[0,0].imshow(Mat, cmap='gray', interpolation='nearest')
axes[0,0].set_title("Original (28x28)")
axes[0,0].axis('off')

axes[0,1].imshow(res_vert, cmap='gray', interpolation='nearest')
axes[0,1].set_title("Sobel Vertical (26x26)")
axes[0,1].axis('off')

axes[0,2].imshow(res_hori, cmap='gray', interpolation='nearest')
axes[0,2].set_title("Sobel Horizontal (26x26)")
axes[0,2].axis('off')

axes[1,0].imshow(res_diago_d, cmap='gray', interpolation='nearest')
axes[1,0].set_title("Sobel Horizontal (26x26)")
axes[1,0].axis('off')

axes[1,1].imshow(res_diago_m, cmap='gray', interpolation='nearest')
axes[1,1].set_title("Sobel Horizontal (26x26)")
axes[1,1].axis('off')

axes[1,2].imshow(res_flou, cmap='gray', interpolation='nearest')
axes[1,2].set_title("Contours (26x26)")
axes[1,2].axis('off')

plt.tight_layout()
plt.show()
