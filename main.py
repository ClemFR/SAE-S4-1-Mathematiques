import util
from matplotlib import pyplot as plt

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
            util.plot(donnees, a, b)
