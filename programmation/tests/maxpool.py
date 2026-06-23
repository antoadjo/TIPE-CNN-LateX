import matplotlib.pyplot as plt

mat = [
    [12, 20, 30,  0],
    [ 8, 12,  2,  3],
    [34, 85,  5,  6],
    [ 9, 10,  4, 27]
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

afficher_matrice(mat)

def MaxPool(mat):
    n = len(mat)
    res = new_mat(n//2)
    for i in range(0, n, 2):
        for j in range(0, n, 2):
            val = []
            for k in range(2):
                for l in range(2):
                    val.append(mat[i + k][j + l])
            val_max = max(val)
            res[i // 2][j // 2] = val_max
    return res

afficher_matrice(MaxPool(mat))