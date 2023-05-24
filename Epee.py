player_name = input("Entrez votre nom : ")
player_level = 1
player_health = 100
player_weapon = "Une épée"
player_armor = "une armure en cuir"

found_items = []
num_found_items = 0

search_result = input("Voulez-vous chercher un trésor ? (oui/non) ")

if search_result == "oui":
    treasure_found = True
    num_found_items += 1
    rep = int(input("Voulez-vous {}(1) ou {}(2) ? Choisissez 1 ou 2 : ".format(player_weapon, player_armor)))

    if rep == 2:
        print("Mauvais choix")
    else:
        print("Excellent choix ! La meilleure défense, c'est l'attaque.")
else:
    treasure_found = False
    print("C'est excellent, je garde tout pour moi.")
