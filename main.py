import util

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
        data.append((line.split()[0], line.split()[1],))

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


if __name__ == "__main__":
    donnees = None
    try:
        donnees = ouvrirFichier("donnees.txt")
    except Exception:
        print("Erreur lors de l'ouverture du fichier")

    if donnees is not None:
        print("Le fichier des données a été ouvert avec succès")
        choix = menu()
        print("Votre choix est : " + str(choix))
