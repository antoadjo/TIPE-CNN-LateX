import matplotlib.pyplot as plt

def new_mat(n):
    return [[0 for _ in range(n)] for _ in range(n)]

def relu(mat):
    res = new_mat(len(mat))
    for i in range(len(mat)):
        for j in range(len(mat)):
            if mat[i][j] < 0 :
                res[i][j] = 0
            else:
                res[i][j] = mat[i][j]
    return res

# # 1. Convolution (Sortie : 26x26 avec des valeurs positives et négatives)
# res_hori = calcul(Mat, flt_hori)    

# # 2. Activation ReLU (Sortie : 26x26, toutes les valeurs négatives deviennent 0)
# res_hori_relu = relu(res_hori)

# # 3. MaxPool (Sortie : 13x13)
# mp_bis_hori = MaxPool(res_hori_relu)