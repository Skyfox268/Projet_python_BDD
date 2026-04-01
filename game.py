import main
import time
import combat_jeu
import combat_jeu
import fin_jeu
import preparation

def start_game():
    print ("Bienvenue dans le jeu de combat !")
    print ("================================")
    print ("Demarrer le jeu... : 1")
    print ("Afficher classement... : 2")
    print ("Quitter le jeu... : 3")
    print ("================================")
    choix = int(input("Entrez votre choix :"))
    if choix == 1:
        deroulement_choix()
    elif choix == 2:
        main.afficher_classement()
    elif choix == 3:
        main.quitter_jeu()
    else:
        print("Choix invalide ! Veuillez réessayer.")
        start_game()

def deroulement_choix():
    pseudo = main.choisir_pseudo()
    equipe = preparation.choisir_equipe()
    noms_equipe = [list(perso.keys())[1] for perso in equipe]
    print(f"Bienvenue {pseudo} ! Votre équipe :")
    for perso in equipe:
        nom = list(perso.keys())[1]
        stats = perso[nom]
        print(f"  - {nom} (PV: {stats['PV']}, ATK: {stats['ATK']}, DEF: {stats['DEF']})")
    combat(equipe, pseudo)

def combat(equipe, pseudo, vague=1):
    monstre_choisi = main.choisir_monstre()
    nom_monstre = list(monstre_choisi.keys())[1]
    print(f"\nUn {nom_monstre} apparaît !")
    print("================================")
    time.sleep(2)

    while not fin_jeu.combat_fini(equipe, monstre_choisi):
        combat_jeu.attack(equipe, monstre_choisi)
        print("================================")
        time.sleep(2)
        if fin_jeu.combat_fini(equipe, monstre_choisi):
            print(f"Vague {vague} terminée !")
            combat(equipe, pseudo, vague + 1)
            return
        combat_jeu.defense(equipe, monstre_choisi)
        print("================================")
        time.sleep(2)
    
    fin_jeu.resultat_combat(equipe, monstre_choisi, pseudo, vague)
    print ("Tu as survécu jusqu'à la vague ", vague)

start_game()

