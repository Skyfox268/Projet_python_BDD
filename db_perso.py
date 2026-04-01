from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['mydatabase']
collection = db["personnages"]

personnages = [
    {"Guerrier": {"ATK": 15, "DEF": 10, "PV": 100}},
    {"Mage": {"ATK": 20, "DEF": 5, "PV": 80}},
    {"Archer": {"ATK": 18, "DEF": 7, "PV": 90}},
    {"Voleur": {"ATK": 22, "DEF": 8, "PV": 85}},
    {"Paladin": {"ATK": 14, "DEF": 12, "PV": 110}},
    {"Sorcier": {"ATK": 25, "DEF": 3, "PV": 70}},
    {"Chevalier": {"ATK": 17, "DEF": 15, "PV": 120}},
    {"Moine": {"ATK": 19, "DEF": 9, "PV": 95}},
    {"Berserker": {"ATK": 23, "DEF": 6, "PV": 105}},
    {"Chasseur": {"ATK": 16, "DEF": 11, "PV": 100}},
    {"Dieu de la guerre": {"ATK": 190, "DEF": 20, "PV": 10000}},
    ]

collection.drop()
collection.insert_many(personnages)

