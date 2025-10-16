"""Controleur principal de l'application."""
from views.main_view import MainView
from views.player_view import PlayerView
from views.tournament_view import TournamentView
from controllers.player_controller import PlayerController
from controllers.tournament_controller import TournamentController


class MainController:
    """Classe principale pour gerer l'application."""

    def __init__(self, db_manager):
        """Initialise le controleur principal."""
        self.db_manager = db_manager
        self.player_controller = PlayerController(db_manager)
        self.tournament_controller = TournamentController(db_manager)

    def show_reports(self):
        """Affiche le menu des rapports."""
        while True:
            choice = MainView.display_reports_menu()
            if choice == '1':
                players = self.db_manager.get_players_sorted_by_name()
                PlayerView.display_players(players, "JOUEURS (PAR ORDRE ALPHABETIQUE)")
            elif choice == '2':
                players = self.db_manager.get_players_sorted_by_ranking()
                PlayerView.display_players(players, "JOUEURS (PAR CLASSEMENT)")
            elif choice == '3':
                tournaments = self.db_manager.get_all_tournaments()
                TournamentView.display_tournaments(tournaments)
            elif choice == '4':
                tournaments = self.db_manager.get_all_tournaments()
                if tournaments:
                    tournament = TournamentView.select_tournament(tournaments)
                    if tournament:
                        TournamentView.display_tournament_details(tournament)
                else:
                    MainView.display_error("Aucun tournoi enregistre.")
            elif choice == '5':
                break
            else:
                MainView.display_error("Choix invalide.")
            MainView.pause()

    def run(self):
        """Boucle principale de l'application."""
        while True:
            choice = MainView.display_main_menu()
            if choice == '1':
                self.player_controller.run()
            elif choice == '2':
                self.tournament_controller.run()
            elif choice == '3':
                self.show_reports()
            elif choice == '4':
                MainView.display_message("Au revoir !")
                self.db_manager.close()
                break
            else:
                MainView.display_error("Choix invalide.")
