import random

class CreatePokemon():

    def __init__(self, name, hit_points, pokemon_type):
        self.name = name.title()
        self.hit_points = hit_points
        self.pokemon_type = pokemon_type.title()

    def describe_pokemon(self):
        print("Your pokemon is: " + self.name)
        print(self.name + ("'s HP is: " + str(self.hit_points)))
        print(self.name + " is a " + self.pokemon_type + " type.")


class Charmander(CreatePokemon):
    def __init__(self, name, hit_points, pokemon_type):
        super().__init__(name, hit_points, pokemon_type)
        self.moves = {'ember': 15, 'fire punch': 20, 'tackle': 10, 'scratch': 6}


class Bulbasaur(CreatePokemon):
    def __init__(self, name, hit_points, pokemon_type):
        super().__init__(name, hit_points, pokemon_type)
        self.moves = {'vine whip': 15, 'razor leaf': 20, 'tackle': 10, 'scratch': 6}


class Squirtle(CreatePokemon):
    def __init__(self, name, hit_points, pokemon_type):
        super().__init__(name, hit_points, pokemon_type)
        self.moves = {'water gun': 15, 'bubblebeam': 20, 'tackle': 100, 'scratch': 6}

#Battle Simulation
def attack(attacker_name, attacker_pokemon, defender_pokemon):
    """Handles the attack logic for a single turn."""
    print(f"{attacker_name}, choose an attack:")
    for i, move in enumerate(attacker_pokemon.moves.keys(), start=1):
        print(f"{i} - {move}")

    while True:
        try:
            choice = int(input("\nChoose your move (1-4): "))
            move_list = list(attacker_pokemon.moves.keys())
            if 1 <= choice <= len(move_list):
                selected_move = move_list[choice - 1]
                damage = attacker_pokemon.moves[selected_move]

                #Check Pokemon type
                if selected_move in ['ember', 'fire punch'] and defender_pokemon.pokemon_type == 'Grass':
                    damage += 20
                    print(f"{attacker_pokemon.name} used {selected_move} and dealt {damage} damage!\nIt's super effective!")
                elif selected_move in ['vine whip', 'razor leaf'] and defender_pokemon.pokemon_type == 'Water':
                    damage += 20
                    print(f"{attacker_pokemon.name} used {selected_move} and dealt {damage} damage!\nIt's super effective!")
                elif selected_move in ['water gun', 'bubblebeam'] and defender_pokemon.pokemon_type == 'Fire':
                    damage += 20
                    print(f"{attacker_pokemon.name} used {selected_move} and dealt {damage} damage!\nIt's super effective!")
                else:
                    print(f"{attacker_pokemon.name} used {selected_move} and dealt {damage} damage!")

                #scratch critical chance
                if selected_move == 'scratch' and random.random() < 0.17:
                    damage *= 3


                defender_pokemon.hit_points -= damage
                print(f"{defender_pokemon.name}'s HP is now: {defender_pokemon.hit_points}")
                return defender_pokemon.hit_points <= 0  # Return True if the defender faints
            else:
                print("Invalid choice. Please select a move from 1 to 4.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")

#Choosing pokemon
def choose_pokemon(player_name, available_pokemon):
    while True:
        print(f"{player_name}, choose your Pokémon: ")
        try:
            choice = input("1 - Charmander\n2 - Bulbasaur\n3 - Squirtle\n")
            if choice == '1' and 'charmander' in available_pokemon:
                available_pokemon.remove('charmander')
                return Charmander('Charmander', 100, 'Fire')
            elif choice == '2' and 'balbasaur' in available_pokemon:
                available_pokemon.remove('balbasaur')
                return Bulbasaur('Bulbasaur', 100, 'Grass')
            elif choice == '3' and 'squirtle' in available_pokemon:
                available_pokemon.remove('squirtle')
                return Squirtle('Squirtle', 100, 'Water')
            else:
                print("Please choose from the available Pokémon.")
        except IndexError:
            print(f"Please choose from the available Pokémon.")

#toss coin feature
def toss_coin(player1_name, player2_name):
    """Simulates a coin toss and determines the winner."""
    tosscoin_random_number = random.randint(1, 2)
    if tosscoin_random_number == 1:
        return "heads", player1_name, player2_name  # (result, winner, loser)
    else:
        return "tails", player2_name, player1_name  # (result, winner, loser)

