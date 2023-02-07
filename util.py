def inputInt(min, max, msg="Veuillez entrer une valeur"):
    """
    Demande à l'utilisateur de rentrer un entier entre min et max
    :param msg: Le message a afficher
    :param min: La valeur minimum
    :param max: La valeur maximum
    :return: L'entier entré par l'utilisateur
    """
    msg = msg + " (" + str(min) + " - " + str(max) + ") : "

    reponseOk = False
    erreur = 0
    while not reponseOk:
        rep = input(msg)
        try:
            if rep.isdigit() and not rep.isspace() and len(rep) != 0:
                rep = int(rep)
                if rep >= min and rep <= max:
                    reponseOk = True
                else:
                    erreur += 1
                    print("Choix incorrect !")
            else:
                erreur += 1
                print("Choix incorrect !")
        except ValueError:
            erreur += 1
            print("Choix incorrect !")

        if erreur >= 5:
            rep = erreur
            reponseOk = True

    return rep