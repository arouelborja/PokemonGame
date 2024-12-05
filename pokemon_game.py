import pokemon_game_classes as pm

active = True

while active:
    print("***Welcome to Pokemon Lite!***")

    player1_name = input("Enter player 1 name: ").title()
    player2_name = input("Enter player 2 name: ").title()
    player1_pokemon = ''
    player2_pokemon = ''

    # Toss coin to determine first pick
    print("Toss coin initiated.")
    toss_result, winner, loser = pm.toss_coin(player1_name, player2_name)
    print(f"{toss_result.title()}! {winner} picks first.")

    available_pokemon = ['charmander', 'balbasaur', 'squirtle']
    # Players choose their Pokémon
    if winner == player1_name:
        player1_pokemon = pm.choose_pokemon(player1_name, available_pokemon)
        player2_pokemon = pm.choose_pokemon(player2_name, available_pokemon)
    else:
        player2_pokemon = pm.choose_pokemon(player2_name, available_pokemon)
        player1_pokemon = pm.choose_pokemon(player1_name, available_pokemon)

    print(f"{player1_name} chose {player1_pokemon.name} - HP: {player1_pokemon.hit_points}")
    print(f"{player2_name} chose {player2_pokemon.name} - HP: {player2_pokemon.hit_points}")

    print("The battle begins!")

    #Battle Simulation
    battle = True
    while battle:
        if pm.attack(player1_name, player1_pokemon, player2_pokemon):
            print(f"{player2_pokemon.name} has fainted! {player1_name} and {player1_pokemon.name} wins!")
            battle = False
            break

        if pm.attack(player2_name, player2_pokemon, player1_pokemon):
            print(f"{player1_pokemon.name} has fainted! {player2_name} and {player2_pokemon.name} wins!")
            battle = False
            break

    play_again = True
    while play_again:
        new_game = input("Start a new game? (y/n): ").lower()
        if new_game == 'y':
            active = True
            play_again = False
        elif new_game == 'n':
            print("Thanks for playing!")
            active = False
            play_again = False
        else:
            print("Please enter a valid input (y/n: ")