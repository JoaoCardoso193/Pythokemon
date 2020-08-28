import time
# import numpy as np
import random
import sys

# Delay printing
def delay_print(s):
    # print one character at a time
    # https://stackoverflow.com/questions/9246076/how-to-print-one-character-at-a-time-on-one-line
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)


#User integer-only input
def int_input(s, limits = []):
    user_input = input(s)
    if user_input == "exit" or user_input == 'Exit':
        exit()
    try:
        if limits != []:
            if int(user_input) >= limits[0] and int(user_input) <= limits[1]:
                return int(user_input)
            else:
                print("Value outside limits!")
                return int_input(s, limits)
        else:
            return int(user_input)
    except:
        print("Must be an integer value!")
        return int_input(s)


# Create the class
class Pokemon:
    Pokemon_index = 0
    Pokemon_num = 0
    Pokemon_list = []
    Pokemon_name_list = []
    player_1_tally = 0
    player_2_tally = 0
    Round = 1


    def __init__(self, name, types, bars, moves, EVs):
        # save variables as attributes
        self.name = name
        self.index = Pokemon.Pokemon_index
        self.types = types
        self.moves = moves
        self.attack = EVs['ATTACK']
        self.attack_value = EVs['ATTACK']
        self.defense = EVs['DEFENSE']
        self.defense_value = EVs['DEFENSE']
        self.speed = EVs['SPEED']
        self.pp = 10
        self.health_value = bars
        self.bars = bars
        self.health = ''
        for i in range(self.bars):
            self.health += '='

        Pokemon.Pokemon_index += 1
        Pokemon.Pokemon_num += 1
        Pokemon.Pokemon_list.append(self)
        Pokemon.Pokemon_name_list.append(self.name)


    def __repr__(self):
        return "(Name = {}, Type = {}, HP = {}, Attack = {}, Defense = {}, Speed = {},  Moves = {}".format( self.name, self.types, self.bars, self.attack, self.defense, self.speed, self.moves)


    def whogoesfirst(Pokemon_1, Pokemon_2):
        battlers = [Pokemon_1, Pokemon_2]
        order = []
        if Pokemon_1.speed > Pokemon_2.speed:
            first = Pokemon_1
            second = Pokemon_2
        elif Pokemon_2.speed > Pokemon_1.speed:
            first = Pokemon_2
            second = Pokemon_1
        elif Pokemon_1.speed == Pokemon_2.speed:
            selector = random.random()
            if selector >= 0.5:
                first = Pokemon_1
                second = Pokemon_2
            else:
                first = Pokemon_2
                second = Pokemon_1
        order.append(first)
        order.append(second)
        return(order)

    def reset_stats(battler_1, battler_2):
        #Resetting health values
        battler_1.bars = battler_1.health_value
        battler_2.bars = battler_2.health_value
        battler_1.health = ""
        battler_2.health = ""
        for i in range(battler_1.bars):
            battler_1.health += '='
        for i in range(battler_2.bars):
                battler_2.health += '='

        #Resetting Attack and Defense values
        battler_1.attack = battler_1.attack_value
        battler_2.attack = battler_2.attack_value
        battler_1.defense = battler_1.defense_value
        battler_2.defense = battler_2.defense_value

        #Resetting PP values
        battler_1.pp = 10
        battler_2.pp = 10

    def fight(Pokemon_1, Pokemon_2, single_player = False):
        #Picking first and second battler
        playersdic = {Pokemon_1: "Player 1", Pokemon_2 : "Player 2"}
        order = Pokemon.whogoesfirst(Pokemon_1, Pokemon_2)
        battler_1 = order[0]
        battler_2 = order[1]

        #Checking that battlers are not the same
        if battler_1.name == battler_2.name:
            print("\nError: A battler can't fight itself!\n")
            time.sleep(2)
            print("\nRestarting game...\n")
            time.sleep(2)
            Pokemon.execute_game()

        # Print fight information
        print("\n--------------------------POKEMON BATTLE, ROUND " + str(Pokemon.Round) + "---------------------------")
        print(f"\n{battler_1.name}")
        print("TYPE:", battler_1.types)
        print("SPEED:", battler_1.speed)
        print("HP:", battler_1.bars)
        print("ATTACK:", battler_1.attack)
        print("DEFENSE:", battler_1.defense)
        # print("LVL/", 3*(1+np.mean([battler_1.attack,battler_1.defense])))
        print("\nVS")
        print(f"\n{battler_2.name}")
        print("TYPE:", battler_2.types)
        print("SPEED:", battler_2.speed)
        print("HP:", battler_2.bars)
        print("ATTACK:", battler_2.attack)
        print("DEFENSE:", battler_2.defense)
        # print("LVL/", 3*(1+np.mean([battler_2.attack,battler_2.defense])))

        time.sleep(5)

        # Consider type advantages
        version = ['Fire', 'Water', 'Grass']
        for i,k in enumerate(version):
            if battler_1.types == k:
                # Both are same type
                if battler_2.types == k:
                    string_1_attack = "\n\n"
                    string_2_attack = "\n\n"

                # battler_2 is STRONG
                if battler_2.types == version[(i+1)%3]:
                    battler_2.attack *= 1.5
                    battler_2.defense *= 1.5
                    battler_1.attack /= 1.5
                    battler_1.defense /= 1.5
                    string_1_attack = "\nIt's not very effective...\n\n"
                    string_2_attack = "\nIt's super effective!\n\n"

                # battler_2 is WEAK
                if battler_2.types == version[(i+2)%3]:
                    battler_1.attack *= 1.5
                    battler_1.defense *= 1.5
                    battler_2.attack /= 1.5
                    battler_2.defense /= 1.5
                    string_1_attack = "\nIt's super effective!\n\n"
                    string_2_attack = "\nIt's not very effective...\n\n"

        # Now for the actual fighting...
        # Continue while Pokemon still have health


        while (battler_1.health != "") and (battler_2.bars != ""):
            # Print the health of each Pokemon
            print("\n--------------------------------------------------------------------------------")
            print(f"\n{battler_1.name}\t\nHP   {battler_1.health}\nPP: {battler_1.pp}\n")
            print(f"{battler_2.name}\t\nHP   {battler_2.health}\nPP: {battler_2.pp}\n")

            print(f"Go {battler_1.name}!")
            for i, x in enumerate(battler_1.moves):
                print(f"[{i+1}]", x)

            if single_player == True: #Random CPU choice if it's CPU's turn
                if playersdic[battler_1] == "Player 2":
                    index = int(random.uniform(1, len(battler_1.moves) + 1))
                    tries = 0
                    while int(battler_1.moves[index-1][2].strip('PP Cost: ')) > battler_1.pp: #selecting move with enough pp unles impossible
                        index = int(random.uniform(1, len(battler_1.moves) + 1))
                        tries += 1
                        if tries == 20:
                            break
                    time.sleep(1)
                else:
                    index = int_input(playersdic[battler_1] + ', pick a move: ', limits = [1, len(battler_1.moves)])
            
            else:
                index = int_input(playersdic[battler_1] + ', pick a move: ', limits = [1, len(battler_1.moves)])
            
            move_used = battler_1.moves[index-1]
            move_strength = int(move_used[1].strip('Strength: '))
            move_pp = int(move_used[2].strip('PP Cost: '))
            #If battler doesn't have enough PP for selected move
            if move_pp > battler_1.pp:
                delay_print('\nNot enough PP!')
                move_used = ['Struggle', 'Strength: 1', 'PP Cost: 0']
                move_strength = int(move_used[1].strip('Strength: '))
                move_pp = int(move_used[2].strip('PP Cost: '))
            battler_1.pp -= move_pp
            delay_print(f"\n{battler_1.name} used {move_used[0]}!")
            time.sleep(1)
            delay_print(string_1_attack)

            # Determine damage
            battler_2.bars -= ((battler_1.attack + move_strength) / 2) * random.uniform(0.7, 1) #average of Pokemon's attack and move strength, randomized between a range.
            battler_2.health = ""

            # Add back bars plus defense boost
            for j in range(int(battler_2.bars+.4*battler_2.defense)):
                battler_2.health += "="

            #check if health is now larger than original, if so, set it to original
            if len(battler_2.health) > battler_2.health_value:
                battler_2.health = ""
                for i in range(battler_2.health_value):
                    battler_2.health += "="

            time.sleep(1)

            print("\n--------------------------------------------------------------------------------")
            print(f"\n{battler_1.name}\t\nHP   {battler_1.health}\nPP: {battler_1.pp}\n")
            print(f"{battler_2.name}\t\nHP   {battler_2.health}\nPP: {battler_2.pp}\n")
            time.sleep(.5)

            # Check to see if Pokemon fainted
            if battler_2.health == "":
                delay_print("\n..." + battler_2.name + " fainted.\n")
                delay_print("\n..." + battler_1.name + " wins!\n")
                time.sleep(1)
                if playersdic[battler_1] == "Player 1":
                    Pokemon.player_1_tally += 1
                elif playersdic[battler_1] == "Player 2":
                    Pokemon.player_2_tally += 1
                print("--------------------------------------------------------------------------------")
                print("\nPlayer 1 score = " + str(Pokemon.player_1_tally))
                print("\nPlayer 2 score = " + str(Pokemon.player_2_tally) + "\n")
                print("--------------------------------------------------------------------------------")
                time.sleep(3)
                break

            # Pokemon_2's turn
            print(f"Go {battler_2.name}!")
            for i, x in enumerate(battler_2.moves):
                print(f"[{i+1}]", x)

            if single_player == True: #Random CPU choice if it's CPU's turn
                if playersdic[battler_2] == "Player 2":
                    index = int(random.uniform(1, len(battler_2.moves) + 1))
                    tries = 0
                    while int(battler_2.moves[index-1][2].strip('PP Cost: ')) > battler_2.pp: #selecting move with enough pp unles impossible
                        index = int(random.uniform(1, len(battler_2.moves) + 1))
                        tries += 1
                        if tries == 20:
                            break
                    time.sleep(1)
                else:
                    index = int_input(playersdic[battler_2] + ', pick a move: ', limits = [1, len(battler_2.moves)])
            
            else:
                index = int_input(playersdic[battler_2] + ', pick a move: ', limits = [1, len(battler_2.moves)])
            
            move_used = battler_2.moves[index-1]
            move_strength = int(move_used[1].strip('Strength: '))
            move_pp = int(move_used[2].strip('PP Cost: '))
            if move_pp > battler_2.pp:
                delay_print('\nNot enough PP!')
                move_used = ['Struggle', 'Strength: 1', 'PP Cost: 0']
                move_strength = int(move_used[1].strip('Strength: '))
                move_pp = int(move_used[2].strip('PP Cost: '))
            battler_2.pp -= move_pp
            delay_print(f"\n{battler_2.name} used {move_used[0]}!")
            time.sleep(1)
            delay_print(string_2_attack)

            # Determine damage
            battler_1.bars -= ((battler_2.attack + move_strength) / 2) * random.uniform(0.7, 1)
            battler_1.health = ""

            # Add back bars plus defense boost
            for j in range(int(battler_1.bars+.4*battler_1.defense)):
                battler_1.health += "="

            #check if health is now larger than original, if so, set it to original
            if len(battler_1.health) > battler_1.health_value:
                battler_1.health = ""
                for i in range(battler_1.health_value):
                    battler_1.health += "="

            time.sleep(1)

            print(f"{battler_1.name}\t\tHP\t{battler_1.health}")
            print(f"{battler_2.name}\t\tHP\t{battler_2.health}\n")
            time.sleep(.5)

            # Check to see if Pokemon fainted
            if battler_1.health == "":
                delay_print("\n..." + battler_1.name + ' fainted.\n')
                delay_print("\n..." + battler_2.name + ' wins!\n')
                time.sleep(1)
                if playersdic[battler_2] == "Player 1":
                    Pokemon.player_1_tally += 1
                elif playersdic[battler_2] == "Player 2":
                    Pokemon.player_2_tally += 1
                print("--------------------------------------------------------------------------------")
                print("\nPlayer 1 score = " + str(Pokemon.player_1_tally))
                print("\nPlayer 2 score = " + str(Pokemon.player_2_tally) + "\n")
                print("--------------------------------------------------------------------------------")
                time.sleep(3)
                break


    #Iterator
    def __iter__(self):
        if self.isempty():
            return None
        else:
            index = 0
            while index <= self.Pokemon_num - 1:
                yield self.items[index]
                index += 1


    #Execution method
    def execute_game(single_player = False):
        print("--------------------------------------------------------------------------------")
        delay_print("\nPlease choose your battlers from the list below:\n")
        time.sleep(1)
        lst = Pokemon.Pokemon_name_list
        full_lst = Pokemon.Pokemon_list
        display_lst = full_lst[:-1]
        for i,j in enumerate(display_lst):
            print(f"\n[{i+1}]", str(j) + ")")
        time.sleep(1)

        #Method to choose battlers:
        def chooser(player_num, choice_num):
            choice = int_input("\nPlayer " + str(player_num) + ", type in the number of your " + str(choice_num) + " battler (no repeats, type '0' for a random choice): \n", limits = [0, Pokemon.Pokemon_num]) - 1
            while choice in choices:
                delay_print("\nThis battler has already been chosen! Please choose another one.\n")
                choice = int_input("\nPlayer " + str(player_num) + ", type in the number of your " + str(choice_num) + " battler (no repeats, type '0' for a random choice): \n", limits = [0, Pokemon.Pokemon_num]) - 1
            if choice == -1:
                choice = int(random.uniform(1, Pokemon.Pokemon_num)-1)
                while choice in choices:
                    choice = int(random.uniform(1, Pokemon.Pokemon_num)-1)
            choices.append(choice)
            return choice

        #Reading user input and choosing battlers
        choices = []

        #Player 1 Choice 1
        player_1_choice_1 = chooser(1, 'first')

        #Player 2 Choice 1
        if single_player == False:
            player_2_choice_1 = chooser(2, 'first')

        #Player 1 Choice 2
        player_1_choice_2 = chooser(1, 'second')

        #Player 2 Choice 2
        if single_player == False:
            player_2_choice_2 = chooser(2, 'second')
        
        #Player 1 Choice 3
        player_1_choice_3 = chooser(1, 'third')

        #Player 2 Choice 3
        if single_player == False:
            player_2_choice_3 = chooser(2, 'third')

        #Single player CPU choices
        if single_player == True:
            player_2_choice_1 = int(random.uniform(1, Pokemon.Pokemon_num)-1) #add +1 to Pokemon.Pokemon_num if you want AI to be able to choose secret Pokemon Nissim
            while player_2_choice_1 in choices:
                player_2_choice_1 = int(random.uniform(1, Pokemon.Pokemon_num)-1)
            choices.append(player_2_choice_1)
            
            player_2_choice_2 = int(random.uniform(1, Pokemon.Pokemon_num)-1)
            while player_2_choice_2 in choices:
                player_2_choice_2 = int(random.uniform(1, Pokemon.Pokemon_num)-1)
            choices.append(player_2_choice_2)
                
            player_2_choice_3 = int(random.uniform(1, Pokemon.Pokemon_num)-1)
            while player_2_choice_3 in choices:
                player_2_choice_3 = int(random.uniform(1, Pokemon.Pokemon_num)-1)
            choices.append(player_2_choice_3)
            

        #Making the rosters
        player_1_roster = []
        player_1_roster.append(globals()[lst[player_1_choice_1]])
        player_1_roster.append(globals()[lst[player_1_choice_2]])
        player_1_roster.append(globals()[lst[player_1_choice_3]])
        # print("player 1 roster", player_1_roster[0].name, player_1_roster[1].name, player_1_roster[2].name)

        player_2_roster = []
        player_2_roster.append(globals()[lst[player_2_choice_1]])
        player_2_roster.append(globals()[lst[player_2_choice_2]])
        player_2_roster.append(globals()[lst[player_2_choice_3]])
        # print("player 2 roster", player_2_roster[0].name, player_2_roster[1].name, player_2_roster[2].name)


        #Check that there's no repetition
        player_1_set = list(set(player_1_roster))
        player_2_set = list(set(player_2_roster))
        if len(player_1_set) != 3 or len(player_2_set) != 3 or player_1_roster[0] == player_2_roster[0] or player_1_roster[1] == player_2_roster[1] or player_1_roster[2] == player_2_roster[2]:
            print("\nError: Multiple equal battlers!")
            time.sleep(2)
            print("\nRestarting game...\n")
            time.sleep(2)
            Pokemon.execute_game()

        #Round 1:
        battler_1 = player_1_roster[0]
        battler_2 = player_2_roster[0]

        #Calling the fight method
        # print("calling fight method with following arguments: ", battler_1.name, battler_2.name)
        time.sleep(2)
        if single_player == False:
            Pokemon.fight(battler_1, battler_2)
        else:
            Pokemon.fight(battler_1, battler_2, single_player = True)
        
        #Updating Round number
        Pokemon.Round += 1

        #Resetting stats
        Pokemon.reset_stats(battler_1, battler_2)

        #Round 2:
        battler_1 = player_1_roster[1]
        battler_2 = player_2_roster[1]

        #Calling the fight method
        time.sleep(2)
        if single_player == False:
            Pokemon.fight(battler_1, battler_2)
        else:
            Pokemon.fight(battler_1, battler_2, single_player = True)

        #Updating Round number
        Pokemon.Round += 1

        #Resetting stats
        Pokemon.reset_stats(battler_1, battler_2)

        #For round 3, check if tally is not the same
        Round_3 = False
        if Pokemon.player_1_tally == 2:
            delay_print("\nPlayer 1 wins!\n")
        if Pokemon.player_2_tally == 2:
            delay_print("\nPlayer 2 wins!\n")
        if Pokemon.player_1_tally == Pokemon.player_2_tally:
             Round_3 = True

        if Round_3:
            battler_1 = player_1_roster[2]
            battler_2 = player_2_roster[2]

            #Calling the fight method
            time.sleep(2)
            if single_player == False:
                Pokemon.fight(battler_1, battler_2)
            else:
                Pokemon.fight(battler_1, battler_2, single_player = True)            
            #determining winner
            if Pokemon.player_1_tally == 2:
                delay_print("\n Player 1 wins!\n")
            if Pokemon.player_2_tally == 2:
                delay_print("\n Player 2 wins!\n")

        #Resetting stats
        Pokemon.reset_stats(battler_1, battler_2)

        #Resetting tallies
        Pokemon.player_1_tally = 0
        Pokemon.player_2_tally = 0

        #Resetting rounds
        Pokemon.Round = 1

        #Play again?
        print("[1] Play Again")
        print("[2] Go to Main Menu")
        print("[3] Exit Game")
        user_choice_3 = int_input("Please choose an option: ", limits = [1, 3])
        if user_choice_3 == 1:
            if single_player == False:
                Pokemon.execute_game()
            else:
                Pokemon.execute_game(single_player = True)
        if user_choice_3 == 2:
            Pokemon.main_menu()
        if user_choice_3 == 3:
            exit()

    #Writing game's instructions
    def instructions():
        print("\nWelcome to Pythokemon! Below is a list of detailed instructions about the game.\n")
        print("\nGeneral: " + "\Pythokemon is a two-player python-based Pokemon battle. The goal of the game is to beat the other opponent's Pokemon in battle. Each player chooses three Pokemon to battle in order of selection. The winner is selected through the best of three rounds. You can play against another player or against a CPU in 'Single Player' mode.\n")
        print("\nControls: " + "\n All actions in this game are performed by typing an integer and pressing the 'Enter' or 'Return' key. Be careful not to type in numbers too quickly or at the same time as text is printing, or the game may crash. You can type 'exit' or 'Exit' at any point in the game to close it.\n")
        print("\nChoosing battlers: " + "\nAt the start of the game, each player must select three Pokemon to join their roster. To select a Pokemon, simply type the number associated with the desired Pokemon in the list of available battlers. Type '0' to select a random Pokemon. Be careful, each Pokemon can only be selected once! If you are playing in 'Single Player' mode, the CPU will choose its roster after you.\n")
        print("\nPokemon attributes: " + "\nPokemon have multiple attributes that affect their performance in battle: \n'Type' = Pokemon can either be of the 'Fire', 'Water', or 'Grass' type. 'Fire' is strong against 'Grass', 'Grass' is strong against 'Water', and 'Water is strong against 'Fire'. A Pokemon with a stronger type against its opponent will deal more damage and take less damage. If opposing Pokemon are of the same type, the amount of damage they deal to each other will be unchanged.\n'HP' = Health. A Pokemon's health value determines how much damage it can take before dying.\n'Attack' = A Pokemon's attack value determines how much damage its attacks will deal.\n'Defense' = A Pokemon's defense value determines how much health will be lost from an attack. A Pokemon with a higher defense value will lose less health from the same attack when compared to a Pokemon with a lower defense value.\n'Speed' = Speed determines which Pokemon will go first at the start of a round. If two Pokemon have the same speed value, the first one to go will be chosen at random.\n")
        print("\nMoves:" + "\nEach Pokemon has its own set of moves that can be seen in the Pokemon selection screen. Each move has a 'Name', 'Strength' value, and 'PP Cost' value. A move's 'Strength' value determines how much damage it deals, and its 'PP Cost' value dictates how much PP is spent every time that move is used. 'PP' stands for 'Power Points', which are necessary to execute a move. Each Pokemon starts with 10 PP, and if they try to use a move which they don't have enough PP for during battle, they'll use a very weak move instead.\n")
        print("\n[1] Return to Main Menu")
        print("[2] Exit Game")
        user_input = int_input("Please choose an option: ", limits = [1,2])

        if user_input == 1:
            Pokemon.main_menu()
        if user_input == 2:
            exit()


    #Making game's main menu
    def main_menu():
        print("--------------------------------------------------------------------------------")
        delay_print("\nWelcome to Pythokemon! \n")
        time.sleep(1)
        print("[1] Play (Single Player)")
        print("[2] Play (Two Players)")
        print("[3] Read Instructions")
        print("[4] Exit Game")
        user_input = int_input("Please choose an option: ", limits = [1,4])

        if user_input == 1:
            Pokemon.execute_game(single_player = True)
        if user_input == 2:
            Pokemon.execute_game()
        if user_input == 3:
            Pokemon.instructions()
        if user_input == 4:
            exit()

#Creating Pokemon
Bulbasaur = Pokemon('Bulbasaur', 'Grass', 20, [['Vine Whip','Strength: 13','PP Cost: 7'], ['Seed Bomb','Strength: 6', 'PP Cost: 3'], ['Razor Leaf', 'Strength: 10', 'PP Cost: 4']], {'ATTACK': 10, 'DEFENSE': 16, 'SPEED': 12})

Charmander = Pokemon('Charmander', 'Fire', 15, [['Dragon Breath','Strength: 15','PP Cost: 5'], ['Fire Fang','Strength: 7', 'PP Cost: 3'], ['Ember', 'Strength: 4', 'PP Cost: 2']], {'ATTACK': 14, 'DEFENSE': 12, 'SPEED': 18})

Squirtle = Pokemon('Squirtle', 'Water', 18, [['Hydro Pump','Strength: 14','PP Cost: 6'], ['Water Gun','Strength: 7', 'PP Cost: 3'], ['Aqua Tail', 'Strength: 4', 'PP Cost: 2']], {'ATTACK': 12, 'DEFENSE': 14, 'SPEED': 16})


Chikorita = Pokemon('Chikorita', 'Grass', 19, [['Magical Leaf','Strength: 10','PP Cost: 5'], ['Solar Beam','Strength: 12', 'PP Cost: 7'], ['Synthesis', 'Strength: 10', 'PP Cost: 3']], {'ATTACK': 10, 'DEFENSE': 15, 'SPEED': 14})

Cyndaquil = Pokemon('Cyndaquil', 'Fire', 16, [['Flame Wheel','Strength: 15','PP Cost: 6'], ['Lava Plume','Strength: 10', 'PP Cost: 4'], ['Roll Out', 'Strength: 4', 'PP Cost: 2']], {'ATTACK': 14, 'DEFENSE': 13, 'SPEED': 17})

Totodile = Pokemon('Totodile', 'Water', 17, [['Rage','Strength: 14','PP Cost: 5'], ['Crunch','Strength: 6', 'PP Cost: 3'], ['Slash', 'Strength: 4', 'PP Cost: 2']], {'ATTACK': 13, 'DEFENSE': 14, 'SPEED': 16})


Treecko = Pokemon('Treecko', 'Grass', 19, [['Energy Ball','Strength: 14','PP Cost: 6'], ['Mega Drain','Strength: 9', 'PP Cost: 4'], ['Quick Attack', 'Strength: 4', 'PP Cost: 2']], {'ATTACK': 14, 'DEFENSE': 14, 'SPEED': 16})

Torchic = Pokemon('Torchic', 'Fire', 14, [['Fire Spin','Strength: 15','PP Cost: 6'], ['Flame Burst','Strength: 10', 'PP Cost: 4'], ['Peck', 'Strength: 4', 'PP Cost: 2']], {'ATTACK': 16, 'DEFENSE': 11, 'SPEED': 19})

Mudkip = Pokemon('Mudkip', 'Water', 18, [['Whirlpool','Strength: 16','PP Cost: 6'], ['Mud Sport','Strength: 9', 'PP Cost: 5'], ['Tackle', 'Strength: 6', 'PP Cost: 2']], {'ATTACK': 14, 'DEFENSE': 14, 'SPEED': 17})


Ho_Oh = Pokemon('Ho Oh', 'Fire', 50, [['Ancient Power','Strength: 20','PP Cost: 6'], ['Sky Attack', 'Strength: 15', 'PP Cost: 3']], {'ATTACK': 20, 'DEFENSE': 20, 'SPEED': 20})


#Main function
def main():
    Pokemon.main_menu()

if __name__ == '__main__':
    main()