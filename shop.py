from playerclass import player

def visit_shop():
    print("Welcome to the shop!")
    print("1. Minor Potion - Heals 0.25 of max hp, costs 15 gold")
    print("2. Major Potion - Heals all of max hp, costs 60 gold")
    print("3. Damage Upgrade: ")
    print("   a. Tier 1 - +5% dmg, cost: 25 gold")
    print("   b. Tier 2 - +10% dmg, cost: 50 gold")
    print("   c. Tier 3 - +15% dmg, cost: 75 gold")
    print("   d. Tier 4 - +20% dmg, cost: 100 gold")
    print("4. Upgrade Max HP: ")
    print("   a. Tier 1 - +5% max hp, cost: 25 gold")
    print("   b. Tier 2 - +10% max hp, cost: 50 gold")
    print("   c. Tier 3 - +15% max hp, cost: 75 gold")
    print("   d. Tier 4 - +20% max hp, cost: 100 gold")
    print("5. Cancel")

    choose = input("What do you want to buy? ")
    if choose == '1':
        if player.gold >= 15:
            player.minor_potions += 1
            player.gold -= 15
            print("You bought a Minor Potion.")
            print(f"Your total gold is now {player.gold}")
        else:
            print("Not enough gold :( ")
    elif choose == '2':
        if player.gold >= 60:
            player.major_potions += 1
            player.gold -= 60
            print("You bought a Major Potion.")
            print(f"Your total gold is now {player.gold}")
        else:
            print("Not enough gold!")
    elif choose == '3':
        upgrade_choose = input("Choose the tier of damage upgrade (a, b, c, d): ")
        upgrade_costs = {'a': 25, 'b': 50, 'c': 75, 'd': 100}
        upgrade_percentages = {'a': 5, 'b': 10, 'c': 15, 'd': 20}

        if upgrade_choose in upgrade_costs:
            cost = upgrade_costs[upgrade_choose]
            percentage = upgrade_percentages[upgrade_choose]
            if player.gold >= cost:
                player.upgrade_damage(percentage)
                player.gold -= cost
                print(f"You upgraded your damage by {percentage}%.")
                print(f"Your total gold is now {player.gold}")
            else:
                print("Not enough gold!")
        else: 
            print("Invlaid choice!")
    elif choose == '4':
        upgrade_choose = input("Choose the tier of max HP upgrade (a, b, c, d): ")
        upgrade_costs = {'a': 25, 'b': 50, 'c': 75, 'd': 100}
        upgrade_percentages = {'a': 5, 'b': 10, 'c': 15, 'd': 20}

        if upgrade_choose in upgrade_costs:
            cost = upgrade_costs[upgrade_choose]
            percentage = upgrade_percentages[upgrade_choose]
            if player.gold >= cost:
                player.upgrade_max_hp(percentage)
                player.gold -= cost
                print(f"You upgraded your max HP by {percentage}%.")
                print(f"Your total gold is now {player.gold}")
            else:
                print("Not enough gold!")
        else:
            print("Invalid choice!")
