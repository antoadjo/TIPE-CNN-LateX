import matplotlib.pyplot as plt

def flatten(mat):
    res = []
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            res.append(mat[i][j])
    return res

def afficher_matrice(matrice):
    largeur_max = max(len(str(element)) for ligne in matrice for element in ligne)
    print("[")
    for ligne in matrice:
        ligne_formatee = " ".join(f"{elem:>{largeur_max}}" for elem in ligne)
        print(f"  [ {ligne_formatee} ]")
    print("]")

flt_vert = [[1,0,-1],
            [2,0,-2],
            [1,0,-1]]

def afficher_vec(vecteur, blocs_de=10):
    print("[")
    for i in range(0, len(vecteur), blocs_de):
        morceau = vecteur[i:i+blocs_de]
        ligne_formatee = " ".join(f"{elem:>4}" for elem in morceau)
        print(f"  {ligne_formatee}")
    print("]")
afficher_matrice(flt_vert)
afficher_vec(flatten(flt_vert))