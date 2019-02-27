game_properties = ["current_score", "high_score", "number_of_lives", "items_in_inventory", "power_ups", "ammo", "enemies_on_screen", "enemy_kills", "enemy_kill_streaks", "minutes_played", "notifications", "achievements"] 

initial_game = {}.fromkeys([item for item in game_properties], 0)
print(initial_game)

#another way of doing item

initial_game = dict.fromkeys(game_properties, 0)  # automatically loops
