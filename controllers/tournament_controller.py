"""Controleur pour la gestion des tournois."""
from models.tournament import Tournament
from views.tournament_view import TournamentView
from views.player_view import PlayerView
from views.main_view import MainView


class TournamentController:
    """Classe pour gerer les actions liees aux tournois."""

    def __init__(self, db_manager):
        """Initialise le controleur des tournois."""
        self.db_manager = db_manager
        self.current_tournament = None

    def create_tournament(self):
        """Cree un nouveau tournoi."""
        tournament_info = TournamentView.get_tournament_info()
        tournament = Tournament(
            name=tournament_info['name'],
            location=tournament_info['location'],
            start_date=tournament_info['start_date'],
            end_date=tournament_info['end_date'],
            description=tournament_info['description']
        )
        MainView.display_message(f"Tournoi '{tournament.name}' cree !")
        self._add_players_to_tournament(tournament)
        self.db_manager.save_tournament(tournament)
        self.current_tournament = tournament
        self._run_tournament()

    def _add_players_to_tournament(self, tournament):
        """Ajoute des joueurs au tournoi."""
        all_players = self.db_manager.get_all_players()
        if len(all_players) < 8:
            MainView.display_error("Il faut au moins 8 joueurs enregistres pour creer un tournoi.")
            return False
        MainView.display_message("Selectionnez 8 joueurs pour le tournoi :")
        while len(tournament.players) < 8:
            MainView.display_message(f"Joueurs selectionnes : {len(tournament.players)}/8")
            player = PlayerView.select_player(all_players)
            if player:
                if player not in tournament.players:
                    tournament.add_player(player)
                    MainView.display_message(f"{player.first_name} {player.last_name} ajoute au tournoi.")
                else:
                    MainView.display_error("Ce joueur est deja dans le tournoi.")
        return True

    def _run_tournament(self):
        """Gere le deroulement d'un tournoi."""
        tournament = self.current_tournament
        if tournament.current_round == 0:
            tournament.generate_first_round_pairs()
            MainView.display_message("Premier tour genere !")
            self.db_manager.save_tournament(tournament)
        while tournament.current_round <= tournament.number_of_rounds:
            current_round = tournament.rounds[tournament.current_round - 1]
            TournamentView.display_round_matches(current_round)
            MainView.pause()
            self._enter_round_results(current_round)
            current_round.mark_as_complete()
            self.db_manager.save_tournament(tournament)
            TournamentView.display_tournament_standings(tournament.players)
            MainView.pause()
            if tournament.current_round < tournament.number_of_rounds:
                tournament.generate_next_round_pairs()
                MainView.display_message(f"Tour {tournament.current_round} genere !")
                self.db_manager.save_tournament(tournament)
            else:
                MainView.display_message("Tournoi termine !")
                TournamentView.display_tournament_standings(tournament.players)
                break

    def _enter_round_results(self, round_obj):
        """Saisit les resultats d'un tour."""
        MainView.display_message("Saisie des resultats :")
        for i, match in enumerate(round_obj.matches, 1):
            print(f"\nMatch {i} : {match.player1.first_name} {match.player1.last_name} vs "
                  f"{match.player2.first_name} {match.player2.last_name}")
            score1, score2 = TournamentView.get_match_result()
            match.set_result(score1, score2)

    def resume_tournament(self):
        """Reprend un tournoi en cours."""
        tournaments = self.db_manager.get_all_tournaments()
        ongoing_tournaments = [t for t in tournaments if t['current_round'] < t['number_of_rounds']]
        if not ongoing_tournaments:
            MainView.display_error("Aucun tournoi en cours.")
            return
        tournament_data = TournamentView.select_tournament(ongoing_tournaments)
        if tournament_data:
            MainView.display_message("Fonctionnalite de reprise en cours de developpement.")

    def view_all_tournaments(self):
        """Affiche tous les tournois."""
        tournaments = self.db_manager.get_all_tournaments()
        TournamentView.display_tournaments(tournaments)

    def run(self):
        """Boucle principale du controleur des tournois."""
        while True:
            choice = MainView.display_tournament_menu()
            if choice == '1':
                self.create_tournament()
            elif choice == '2':
                self.resume_tournament()
            elif choice == '3':
                self.view_all_tournaments()
            elif choice == '4':
                break
            else:
                MainView.display_error("Choix invalide.")
            MainView.pause()
