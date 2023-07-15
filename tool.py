import json, random

with open('./data/stats.json', 'r') as file:
    data = json.load(file)


rarity = data["Rarity"]
quality = data["quality"]
nebeneffekte = data["nebeneffekte"]
nebeneffekte_weights = data["nebeneffekte_weights"]
damage_types = data["damage_types"]
ability_score = data["ability_score"]


def gen_effekt(sel_rarity):
    roll = None
    if "-" in str(rarity[sel_rarity][-1]["weights"]):
            roll = get_ran_num(1, int(rarity[sel_rarity][-1]["weights"].split("-")[1]))
    else:
        roll = get_ran_num(1, int(rarity[sel_rarity][-1]["weights"]))

    #print(roll)
    effekt = None
    for rar in rarity[sel_rarity]:
        if "-" in rar["weights"]:
            num = rar["weights"].split("-")
            if int(num[0]) <= roll and int(num[1]) >= roll:
                effekt = rar["Effekt"]
                break
        elif int(rar["weights"]) == roll:
            
            effekt = rar["Effekt"]
            break
        else:
            continue
    return "Es wurde ein {0} Öl generiert. \nDer Effekt des Öl's ist: {1}".format(sel_rarity, effekt)

def get_quallity():
    attk_uses = None
    other_uses = None
    roll = get_ran_num(1,100)
    for e in quality["Attacks"]:
        num = e["Roll"].split("-")
        if int(num[0]) <= roll and int(num[1]) >= roll:
                attk_uses = e["uses"]
                break
        
    for e in quality["Other"]:
        num = e["Roll"].split("-")
        if int(num[0]) <= roll and int(num[1]) >= roll:
                other_uses = e["uses"]
                break

    return "Attack uses: {0} | Other uses: {1}".format(attk_uses, other_uses)

def get_nebeneffekt():
    if get_ran_num(1,100) <= 75:
        schweregrad = None
        effekt = None
        roll = get_ran_num(1,100)
        for s in nebeneffekte_weights["weights"]:
            num = s["weights"].split("-")
            if int(num[0]) <= roll and int(num[1]) >= roll:
                    schweregrad = s["name"]
                    break
            
        roll = None
        if "-" in str(nebeneffekte[schweregrad][-1]["Roll"]):
            roll = get_ran_num(1, int(nebeneffekte[schweregrad][-1]["Roll"].split("-")[1]))
        else:
            roll = get_ran_num(1, nebeneffekte[schweregrad][-1]["Roll"])

        #print("Schweregrad: {0} | Roll {1}".format(schweregrad, roll))

        for n in nebeneffekte[schweregrad]:
            num = None
            if "-" in str(n["Roll"]):
                num = n["Roll"].split("-")
                if int(num[0]) <= roll and int(num[1]) >= roll:
                    effekt = n["Effekt"]
                    break
            else:
                if n["Roll"] == roll:
                    effekt = n["Effekt"]
                    break

        return "Das Öl hat den Nebeneffekt: {0}".format(effekt)
    else:
        return "Das Öl hat keien Nebeneffekt"

def get_random_damage_type():
    return "Das Öl hat den Random Damage Type {0}".format(random.choice(damage_types))

def get_random_ability_score():
    ras = random.sample(ability_score, 2)
    return "Das Öl hat die Random Ability Scores {0} und {1}".format(ras[0], ras[1])

def get_ran_num(von, bis):
    return random.randint(von, bis)

def get_rarity_input():
    count = 1
    for r in rarity:
        print(count , r)
        count += 1
    inp = input("Gib die rarity an: ")
    match int(inp):
        case 1:
            return "Common"
        case 2:
            return "Uncommon"
        case 3:
            return "Rare"
        case 4:
            return "Very rare"
        case 5:
            return "Legendary"
        
def ask_ammount():
    inp = input("Mehr als 1 item? ")
    if inp in {"Ja","ja","JA","1","Yes","yes","YES","J","j","Y","y"}:
        gen_Multiple_items(input("Wie viele Common?"),input("Wie viele Uncommon?"),input("Wie viele Rare?"),input("Wie viele Very rare?"),input("Wie viele Legendary?"))
    else:
        gen_item(get_rarity_input())

def gen_item(rarity):
    p_effekt = gen_effekt(rarity)
    p_quality = get_quallity()
    p_nebeneffekt = get_nebeneffekt()
    p_random_damage_type = get_random_damage_type()
    p_random_ability_score = get_random_ability_score()

    print(p_effekt)
    print(p_quality)
    print(p_nebeneffekt)
    print(p_random_damage_type)
    print(p_random_ability_score)
    print("\n")

def gen_Multiple_items(common, uncommon, rare, very_rare, legendary):
    for i in range(int(common)):
        gen_item("Common")
    for i in range(int(uncommon)):
        gen_item("Uncommon")
    for i in range(int(rare)):
        gen_item("Rare")
    for i in range(int(very_rare)):
        gen_item("Very rare")
    for i in range(int(legendary)):
        gen_item("Legendary")


ask_ammount()
