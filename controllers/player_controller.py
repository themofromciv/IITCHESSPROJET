"""Controleur pour la gestion des joueurs."""
from models.player import Player
from views.player_view import PlayerView
from views.main_view import MainView


class PlayerController:
    """Classe pour gerer les actions liees aux joueurs."""

    def __init__(self, db_manager):
        """Initialise le controleur des joueurs."""
        self.db_manager = db_manager

    def add_player(self):
        """Ajoute un nouveau joueur a la base de donnees."""
        player_info = PlayerView.get_player_info()
        player = Player(
            first_name=player_info['first_name'],
            last_name=player_info['last_name'],
            birth_date=player_info['birth_date'],
            gender=player_info['gender'],
            ranking=player_info['ranking']
        )
        self.db_manager.save_player(player)
        MainView.display_message(f"Joueur {player.first_name} {player.last_name} ajoute avec succes !")

    def update_player_ranking(self):
        """Met a jour le classement d'un joueur."""
        players = self.db_manager.get_all_players()
        if not players:
            MainView.display_error("Aucun joueur enregistre.")
            return
        player = PlayerView.select_player(players)
        if player:
            new_ranking = PlayerView.get_new_ranking()
            self.db_manager.update_player_ranking(player, new_ranking)
            MainView.display_message(f"Classement de {player.first_name} {player.last_name} "
                                     f"mis a jour a {new_ranking}.")

    def view_all_players(self):
        """Affiche tous les joueurs."""
        players = self.db_manager.get_all_players()
        PlayerView.display_players(players)

    def run(self):
        """Boucle principale du controleur des joueurs."""
        while True:
            choice = MainView.display_player_menu()
            if choice == '1':
                self.add_player()
            elif choice == '2':
                self.update_player_ranking()
            elif choice == '3':
                self.view_all_players()
            elif choice == '4':
                break
            else:
                MainView.display_error("Choix invalide.")
            MainView.pause()
