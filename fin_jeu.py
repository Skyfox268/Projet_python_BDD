import main

def combat_fini(equipe, monstre_choisi):
    """Retourne True si le combat est terminé."""
    nom_monstre = list(monstre_choisi.keys())[1]
    if monstre_choisi[nom_monstre]['PV'] <= 0:
        return True
    # Vérifie si tous les persos sont morts
    vivants = [p for p in equipe if p[list(p.keys())[1]]['PV'] > 0]
    if len(vivants) == 0:
        print("💀 Toute votre équipe est éliminée !")
        return True
    return False

def resultat_combat(equipe, monstre_choisi, pseudo, vague=1):
    """Affiche le résultat et enregistre le score."""
    nom_perso = list(equipe[0].keys())[1]
    nom_monstre = list(monstre_choisi.keys())[1]
    if monstre_choisi[nom_monstre]['PV'] <= 0:
        main.db["classement"].insert_one({"pseudo": pseudo, "score": 0})
    else:
        print(f"💀 Dommage ! Vous avez perdu le combat !")
        main.db["classement"].insert_one({"pseudo": pseudo, "score": vague ** 2})