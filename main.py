import random
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client["mydatabase"]

def quitter_jeu():
    print ("Merci d'avoir joué ! À bientôt !")
    exit()

def afficher_classement():
    print ("Voici le classement des joueurs :")
    joueurs = list(db["classement"].find().sort("score", -1))
    for i, joueur in enumerate(joueurs):
        print(f"{i + 1}. {joueur['pseudo']} - Score : {joueur['score']}")


def choisir_pseudo():
    print ("Avant de commencer, veuillez choisir votre pseudo.")
    pseudo = input("Entrez votre pseudo :")
    return pseudo

def team_complete(equipe):
    if len(equipe) == 3:
        return True
    return False

def choisir_monstre():
    monstres = list(db["monstres"].find())
    monstre_choisi = random.choice(monstres)
    return monstre_choisi




