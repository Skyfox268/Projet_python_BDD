from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['mydatabase']
collection = db["monstres"]

monstres = [
    {"Gobelin": {"ATK": 10, "DEF": 5, "PV": 50}},
    {"Orc": {"ATK": 20, "DEF": 8, "PV": 120}},
    {"Dragon": {"ATK": 35, "DEF": 20, "PV": 300}},
    {"Zombie": {"ATK": 12, "DEF": 6, "PV": 70}},
    {"Troll": {"ATK": 25, "DEF": 15, "PV": 200}},
    {"Spectre": {"ATK": 18, "DEF": 10, "PV": 100}},
    {"Golem": {"ATK": 30, "DEF": 25, "PV": 250}},
    {"Vampire": {"ATK": 22, "DEF": 12, "PV": 150}},
    {"Loup-garou": {"ATK": 28, "DEF": 18, "PV": 180}},
    {"Squelette": {"ATK": 15, "DEF": 7, "PV": 90}},
    {"Lisa": {"ATK": 1, "DEF": 0, "PV": 10}}
]

collection.insert_many(monstres)
