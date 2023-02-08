import util
import math

def ouvrirFichier(file: str):
    """
    Permet de lire un fichier et de le retourner sous forme de liste
    :param file: Le chemin du fichier à lire
    :return: Un tableau contenant des tuples
    """
    f = open(file, "r")
    donnees = f.readlines()
    f.close()

    data = []
    for line in donnees:
        data.append((float(line.split()[0]), float(line.split()[1]),))

    return data


def menu():
    """
    Permet de créer un menu pour l'utilisateur
    :return: Le choix de l'utilisateur
    """
    print("1. Résolution linéaire par résolution analytique")
    print("2. Régression linéaire par descente de gradient")
    print("3. Quitter")
    choix = util.inputInt(1, 3)

    return choix


def resolv_analytique(donnees):
    sum_x = 0
    sum_y = 0
    sum_pow_x = 0
    sum_xy = 0

    for x, y in donnees:
        sum_x += x
        sum_y += y
        sum_pow_x += x ** 2
        sum_xy += x * y

    avg_x = sum_x / len(donnees)
    avg_y = sum_y / len(donnees)
    avg_pow_x = sum_pow_x / len(donnees)
    avg_xy = sum_xy / len(donnees)

    a = (avg_xy - avg_x * avg_y) / (avg_pow_x - avg_x ** 2)
    b = avg_y - a * avg_x

    return a, b


def axb(a, b, x):
    return a*x+b


def resolv_desc_grad(donnees, a=1, b=1, err=0.0001, max_iter=1000000, alpha=0.00001):
    # Calcul des valeurs pour les gradients
    xi2 = 0
    xi = 0
    xi_yi = 0
    yi = 0

    for x, y in donnees:
        xi2 += x ** 2
        xi += x
        yi += y
        xi_yi += x * y

    fin = False
    i = 0
    while not fin:
        cout = calcul_cout(donnees, a, b)
        if cout <= err:
            fin = True
            print("Cout : " + str(cout))
        else:
            # Calcul du vecteur gradient
            grad_a = deriver_a(xi2, xi, xi_yi, a, b)
            grad_b = deriver_b(xi, yi, len(donnees), a, b)

            if abs(grad_a) < err and abs(grad_b) < err:
                fin = True
                print("FINITO PIPO. Cout : " + str(cout))

            a -= grad_a * alpha
            b -= grad_b * alpha
            # print("[" + str(i) + "] a = " + str(a) + " b = " + str(b) + " cout = " + str(cout) + " vecteur gradient = (" + str(grad_a) + ", " + str(grad_b) + ") alpha = " + str(alpha) + " longueur vect = " + str(math.sqrt(grad_a ** 2 + grad_b ** 2)))
            i += 1

        if i >= max_iter:
            fin = True
            print("Nombre d'itérations maximum atteint !")

    return a, b


def deriver_a(xi2, xi, xi_yi, a, b):
    return 2 * (xi2 * a + xi * b - xi_yi)


def deriver_b(xi, yi, n, a, b):
    return 2 * (a * xi + b * n - yi)


def calcul_cout(donnees, a, b):
    sum = 0
    for x, y in donnees:
        sum += (y - axb(a, b, x)) ** 2

    return sum



if __name__ == "__main__":
    donnees = None
    try:
        donnees = ouvrirFichier("donnees.txt")
    except Exception as e:
        print(e)
        print("Erreur lors de l'ouverture du fichier")

    if donnees is not None:
        print("Le fichier des données a été ouvert avec succès")
        choix = menu()
        print("Votre choix est : " + str(choix))
        if choix == 1:
            (a,b,) = resolv_analytique(donnees)
            print("a = " + str(a) + " b = " + str(b))
            util.plot(donnees, [(a, b)])
        elif choix == 2:
            (a,b,) = resolv_desc_grad(donnees)
            print("a = " + str(a) + " b = " + str(b))
            c,d = resolv_analytique(donnees)
            util.plot(donnees, [(c, d, "green"), (a, b, "red")])

