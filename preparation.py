import db_perso
import main
import db_perso

def get_personnages():
    return list(db_perso.db["personnages"].find())

def afficher_personnages(personnages=None):
    print ("Voici les personnages disponibles :")
    print ("--------------------------------")
    if personnages is None:
        # retourne une liste vide
        return []
    for i, perso in enumerate(personnages):
        nom = [k for k in perso.keys() if k != "_id"][0]
        stats = perso[nom]
        print(f"{i + 1}. {nom} (PV: {stats['PV']}, ATK: {stats['ATK']}, DEF: {stats['DEF']})")


def choisir_equipe():
    equipe = []
    print ("Choisissez votre équipe de 3 personnages parmi les suivants :")
    personnages = get_personnages()
    afficher_personnages(personnages)
    while not main.team_complete(equipe):
        choix = int(input("Entrez le numéro du personnage que vous souhaitez ajouter à votre équipe :"))
        if 0<= choix <= len(personnages)-1:
            if personnages[choix-1] in equipe:
                print("Ce personnage est déjà dans votre équipe ! Choisissez-en un autre.")
            else:
                equipe.append(personnages[choix-1])
        else:
            print("Choix invalide ! ")
            
    return equipe
