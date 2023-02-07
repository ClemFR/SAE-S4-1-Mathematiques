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



if __name__ == "__main__":
    print(ouvrirFichier("donnees.txt"))