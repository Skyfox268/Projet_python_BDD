import random

def attack(equipe, monstre_choisi):
    nom_monstre = list(monstre_choisi.keys())[1]
    for perso in equipe:
        nom_perso = list(perso.keys())[1]
        if perso[nom_perso]['PV'] > 0:
            degats = perso[nom_perso]['ATK']
            monstre_choisi[nom_monstre]['PV'] -= degats
            print(f"⚔️  {nom_perso} attaque {nom_monstre} et inflige {degats} dégâts !")
    print(f"   {nom_monstre} possède maintenant {monstre_choisi[nom_monstre]['PV']} PV")

def defense(equipe, monstre_choisi):
    nom_monstre = list(monstre_choisi.keys())[1]
    # Le monstre attaque un perso vivant au hasard
    vivants = [p for p in equipe if p[list(p.keys())[1]]['PV'] > 0]
    if vivants:
        cible = random.choice(vivants)
        nom_cible = list(cible.keys())[1]
        degats = monstre_choisi[nom_monstre]['ATK']
        cible[nom_cible]['PV'] -= degats
        print(f"👹 {nom_monstre} attaque {nom_cible} et inflige {degats} dégâts !")
        print(f"   {nom_cible} possède maintenant {cible[nom_cible]['PV']} PV")

def changement_perso(equipe):
    nom_perso = list(equipe[0].keys())[1]
    print(f"💀 {nom_perso} est K.O. !")
    equipe.pop(0)
    if len(equipe) > 0:
        nouveau = list(equipe[0].keys())[1]
        print(f" {nouveau} entre en combat !")
        return True
    else:
        print("💀 Toute votre équipe est éliminée !")
        return False