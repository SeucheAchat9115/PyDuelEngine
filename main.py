from pyduelengine.game.game import Game

if __name__ == "__main__":
    
    game = Game(
        player_1_name="Alice",
        player_1_deck_list="decks/Branded_Dracotail.ydk",
        player_2_name="Bob",
        player_2_deck_list="decks/Mitsurugi.ydk"
    )
    game.start()
