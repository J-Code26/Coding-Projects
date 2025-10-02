#Declare the Python Module
import random
#Globel Constants

MONSTER_COUNT = 0
TREASURE_COUNT = 0
HEALTH = 10
STRENGTH = 0
MANA = 1
EMBER = 1
AQUA = 1
WEAPONS_INV = 0
EXPERIENCE = 0
ENCOUNT = 0
INVENTORY = []

ORIGINAL_MOVE_LIST = ['slime', 'blank', 'slime', 'blank', 'slime', 'blank',
                'chest', 'slime', 'slime', 'slime', 'blank', 'chest', 'chest', 'chest','chest',
                'beefy chest','beefy chest', 'power merchant', 'flame slime',
                'water slime', 'power merchant', 'magic slime', 'flame slime',
                'water slime', 'magic slime', 'goblin', 'giant', 'injured wolf']

#weapon function
def WEAPONS():
    global STRENGTH, WEAPONS_INV, INVENTORY
    weapon_names = ['Battle Axe', 'Sword', 'Mace', 'Spear', 'Dagger', 'Stick', 'Swiss Army Knife']
    weapon_strength = [4,3,3,3,2,1,1]
    i = random.randint(0,len(weapon_strength)-1)
    weapon_output = [weapon_names[i], weapon_strength[i]]
    if weapon_output[1] == 1:
        STRENGTH += 1
        WEAPONS_INV += 1
    elif weapon_output[1] == 2:
        STRENGTH += 2
        WEAPONS_INV += 1
    elif weapon_output[1] == 3:
        STRENGTH += 3
        WEAPONS_INV += 1
    elif weapon_output[1] == 4:
        STRENGTH += 4
        WEAPONS_INV += 1
    INVENTORY.append(weapon_output[0])
    print(f'Strength: {STRENGTH}')
    print(f'Inventory: {INVENTORY}')
#Reset the list of Encounters
def reset_move_list():
    global move_list
    move_list = ORIGINAL_MOVE_LIST.copy()
#Just something that makes it easier to print the stats
def STATUS():
    global HEALTH, STRENGTH, EXPERIENCE, MONSTER_COUNT, ENCOUNT, MANA, EMBER, AQUA, INVENTORY, TREASURE_COUNT
    print('Monster Kills:',MONSTER_COUNT)
    print('Treasure Count:', TREASURE_COUNT)
    print('Health:', HEALTH)
    print('Strength:', STRENGTH)
    print('Mana:', MANA)
    print('Ember:', EMBER)
    print('Aqua:', AQUA)
    print('Experience:', EXPERIENCE)
    print('Inventory:', INVENTORY)
    return
def initial():
    global HEALTH, STRENGTH, EXPERIENCE, MONSTER_COUNT, ENCOUNT, MANA, EMBER, AQUA, INVENTORY, TREASURE_COUNT
    MONSTER_COUNT = 0
    TREASURE_COUNT = 0
    HEALTH = 10
    STRENGTH = 0
    MANA = 1
    EMBER = 1
    AQUA = 1
    EXPERIENCE = 0
    ENCOUNT = 0
    INVENTORY = []
#Main Function
def dungeon():
    global HEALTH, STRENGTH, EXPERIENCE, MONSTER_COUNT, ENCOUNT, MANA, EMBER, AQUA, INVENTORY, TREASURE_COUNT
    print('You have arrived at the dungeon')
    STATUS()
    print()
    print('In order to complete the dungeon, you must reach 15 EXPERIENCE.')
    move_list = ['slime', 'blank', 'slime', 'blank', 'slime', 'blank',
                'chest', 'slime', 'slime', 'slime', 'blank', 'chest', 'chest', 'chest','chest',
                'beefy chest','beefy chest', 'power merchant', 'flame slime',
                'water slime', 'power merchant', 'magic slime', 'flame slime',
                'water slime', 'magic slime', 'goblin', 'giant', 'injured wolf']
        
    direction_list = ['W', 'w', 'quit']
        
    power_list = ['mana', 'ember', 'aqua']
    while True:
        if HEALTH < 1:
            print('You have no health left! Game Over!')
            reset_move_list()
            initial()
            return startup()
        next_move = input('Make your next move(W(advance)/status/quit):')
        if next_move == 'status':
            STATUS()
            continue
        if next_move == 'quit':
            print('Thanks for playing!')
            return
        if next_move not in direction_list:
            print('Please enter a either "w", "status", or "quit".')
            continue
        random_encounter = random.choice(move_list)
        if random_encounter == 'blank':
            print('You advanced, but nothing was in sight')
        else:
            print('You advanced')
        if EXPERIENCE > 14:
            print('Congrats! You completed the dungeon game!')
            print('These are your final stats!:')
            reset_move_list()
            STATUS()
            initial()
            return startup()
            
        if len(move_list) < 5:
            print('Game Over! There are no more enemies left in the dungeon.')
            reset_move_list()
            initial()
            return startup()
# First Encounter
        if ENCOUNT == 0 and random_encounter != 'blank':
            ENCOUNT += 1
            TREASURE_COUNT += 1
            print('You came across the starter chest!')
            EXPERIENCE += 1
            print('Experience:', EXPERIENCE)
            continue
# Slime Encounter
        if random_encounter == 'slime':
            ENCOUNT += 1
            move_list.remove('slime')
            if STRENGTH > 0 or MANA > 1 or EMBER > 1 or AQUA > 1:
                EXPERIENCE += 1
                MONSTER_COUNT += 1
                print('You encountered a slime! You removed it from this world with your strength.')
                print('Experience:', EXPERIENCE)
            else:
                HEALTH -= 1
                print('You encountered a slime! It took some of your health and hopped to wherever it came from!')
                print('Health:', HEALTH)
# Chest Encounter
        if random_encounter == 'chest':
            ENCOUNT += 1
            TREASURE_COUNT += 1
            move_list.remove('chest')
            if STRENGTH < 5:
                print('You found a chest! It has a weapon inside!')
                WEAPONS()
            else:
                print("You found a chest! But it's empty, sorry!")
# Power Merchant Encounter
        if random_encounter == 'power merchant':
            ENCOUNT += 1
            move_list.remove('power merchant')
            print('You encountered a Power Buff Merchant!')
        
            while True:
                print('Experience:', EXPERIENCE)
                trading_input = input('Type yes/no if you would like to recieve a POWER BUFF in return for your EXPERIENCE:')
                if trading_input not in ['yes', 'no']:
                    print('Please enter either "yes" or "no".')
                else:
                    break

            if trading_input == 'yes':
                if EXPERIENCE < 1:
                    print('You have no experience to trade with.')
                else:
                    EXPERIENCE -= 1
                    if random.choice(power_list) == 'mana':
                        MANA += 1
                        print('Mana:', MANA)
                        print('Experience:', EXPERIENCE)
                    elif random.choice(power_list) == 'ember':
                        EMBER += 1
                        print('Ember:', EMBER)
                        print('Experience:', EXPERIENCE)
                    else:
                        AQUA += 1
                        print('Aqua:', AQUA)
                        print('Experience:', EXPERIENCE)

            elif trading_input == 'no':
                print('You decided not to trade with the Power Buff Merchant.')
#Rare Chest Encounter
        if random_encounter == 'beefy chest':
            ENCOUNT += 1
            TREASURE_COUNT += 1
            move_list.remove('beefy chest')
            if STRENGTH < 10:
                print('You found a rare chest! It has a weapon and a status buff!')
                WEAPONS()
                if random.choice(power_list) == 'mana':
                    MANA += 1
                    print('Mana:', MANA)
                elif random.choice(power_list) == 'ember':
                    EMBER += 1
                    print('Ember:', EMBER)
                else:
                    AQUA += 1
                    print('Aqua:', AQUA)
            else:
                print("You found a rare chest! But it's empty, sorry!")
#Flame SLime Encounter
        if random_encounter == 'flame slime':
            ENCOUNT += 1
            move_list.remove('flame slime')
            if STRENGTH > 2 or AQUA > 1 or MANA > 1:
                print('You came across a Flame Slime and removed it from this level!')
                EXPERIENCE += 1
                MONSTER_COUNT += 1
                EMBER += 1
                print('Experience:', EXPERIENCE)
                print('Ember:', EMBER)
            else:
                print('You came across a Flame Slime! It saw how weak you are and took advantage!')
                HEALTH -= 2
                print('Health:', HEALTH)
#Magic Slime Encounter
        if random_encounter == 'magic slime':
            ENCOUNT += 1
            move_list.remove('magic slime')
            if STRENGTH > 2 or EMBER > 1 or AQUA > 1:
                print('You came across a Magic Slime! Because of your skills, it decided not to mess with you and left a POWER Buff behind!')
                EXPERIENCE += 1
                MONSTER_COUNT += 1
                MANA += 1
                print('Experience:', EXPERIENCE)
                print('Mana:', MANA)
            else:
                HEALTH -= 2
                print('You came across a Magic Slime! It took some of your health and disappeared magically!')
                print('Health:', HEALTH)
#Water Slime Encounter
        if random_encounter == 'water slime':
            ENCOUNT += 1
            move_list.remove('water slime')
            if STRENGTH > 1 or EMBER > 1 or MANA > 1:
                print('You came across a Water Slime! You defeated it and it left a damp POWER buff behind!')
                EXPERIENCE += 1
                MONSTER_COUNT += 1
                AQUA += 1
                print('Experience:', EXPERIENCE)
                print('Aqua:', AQUA)
            else:
                HEALTH -= 2
                print("You came across a Water Slime! It sprayed you with it's weird looking goo and took your health!")
                print('Health:', HEALTH)
#Goblin Encounter
        if random_encounter == 'goblin':
            ENCOUNT += 1
            move_list.remove('goblin')
            if STRENGTH > 2 or MANA > 2 or EMBER > 2 or AQUA > 2:
                print('You came across a Goblin! You defeated it with ease and went on your way!')
                EXPERIENCE += 1
                STRENGTH += 1
                MONSTER_COUNT += 1
                print('Experience:', EXPERIENCE)
                print('Strength:', STRENGTH)
            else:
                print("You came across a Goblin! It took a large amount of health and snorted its' way to the hole it came from!")
                HEALTH -= 3
                print('Health:', HEALTH)
#Giant Encounter
        if random_encounter == 'giant':
            ENCOUNT += 1
            move_list.remove('giant')
            while True:
                print('Strength:', STRENGTH)
                battle_input = input('Type yes/no if you would like to fight the FIERCE GIANT:')
            
                if battle_input not in ['yes', 'no']:
                    print('Please enter either "yes" or "no".')
                else:
                    break

            if battle_input == 'yes':
                if STRENGTH > 5 or MANA > 3 or EMBER > 3 or AQUA > 3:
                    print('You encountered a Giant! After a long battle, you defeated it!')
                    EXPERIENCE += 3
                    MONSTER_COUNT += 1
                    STRENGTH += 1
                    print('Experience:', EXPERIENCE)
                    print('Strength:', STRENGTH)
                else:
                    HEALTH -= 5
                    print('The giant took a large amount of your health and stomped away!')
                    print('Health:', HEALTH)

            elif battle_input == 'no':
                print('You narrowly escaped from the giant!')
#Injured Wolf Encounter
        if random_encounter == 'injured wolf':
            ENCOUNT += 1
            move_list.remove('injured wolf')
            while True:
                print('You have encountered an injured wolf! Would like to help or kill the wolf?')
                encount_input = input('Type h/k if you would to help or kill the wolf:')
                
                if encount_input not in ['h', 'k', 'kill', 'help']:
                    print('Please enter either "h" or "k".')
                else:
                    break
                
            if encount_input in ['h', 'help']:
                STRENGTH += 1
                print('Because you helped the wolf, it gave you a weapon!')
                WEAPONS()
            elif encount_input in ['k', 'kill']:
                print('You decided to kill the innocent wolf and gained some experience.')
                EXPERIENCE += 1
                print('Experience:', EXPERIENCE)
                    
#Call The Function
def startup():
    reset_move_list()
    while True:
        user_input = input('Make your first move(enter/quit):')
        if user_input == 'enter':
            dungeon()
            continue
        elif user_input == 'quit':
            print('Please come back again!')
            return
        else:
            print("Please enter either 'enter' or 'quit'")
print('Welcome to the Dungeon Adventure Game!')
#Call the start screen   
startup()