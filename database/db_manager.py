"""Gestionnaire de base de données avec TinyDB."""
from tinydb import TinyDB, Query
from models.player import Player


class DatabaseManager:
    """Classe pour gérer la persistance des données avec TinyDB."""

    def __init__(self, db_path='chess_tournament.json'):
        """
        Initialise la connexion à la base de données.
        Args:
            db_path (str): Chemin vers le fichier de base de données
        """
        self.db = TinyDB(db_path)
        self.players_table = self.db.table('players')
        self.tournaments_table = self.db.table('tournaments')

    def save_player(self, player):
        """Sauvegarde un joueur dans la base de données."""
        Player_query = Query()
        existing = self.players_table.search(
            (Player_query.first_name == player.first_name) &
            (Player_query.last_name == player.last_name) &
            (Player_query.birth_date == player.birth_date)
        )
        if existing:
            self.players_table.update(
                player.serialize(),
                (Player_query.first_name == player.first_name) &
                (Player_query.last_name == player.last_name) &
                (Player_query.birth_date == player.birth_date)
            )
        else:
            self.players_table.insert(player.serialize())

    def get_all_players(self):
        """Récupère tous les joueurs de la base de données."""
        players_data = self.players_table.all()
        return [Player.deserialize(data) for data in players_data]

    def get_players_sorted_by_name(self):
        """Récupère tous les joueurs triés par nom."""
        players = self.get_all_players()
        return sorted(players, key=lambda p: (p.last_name, p.first_name))

    def get_players_sorted_by_ranking(self):
        """Récupère tous les joueurs triés par classement."""
        players = self.get_all_players()
        return sorted(players, key=lambda p: p.ranking, reverse=True)

    def update_player_ranking(self, player, new_ranking):
        """Met à jour le classement d'un joueur."""
        player.ranking = new_ranking
        self.save_player(player)

    def save_tournament(self, tournament):
        """Sauvegarde un tournoi dans la base de données."""
        Tournament_query = Query()
        existing = self.tournaments_table.search(
            (Tournament_query.name == tournament.name) &
            (Tournament_query.start_date == tournament.start_date)
        )
        if existing:
            self.tournaments_table.update(
                tournament.serialize(),
                (Tournament_query.name == tournament.name) &
                (Tournament_query.start_date == tournament.start_date)
            )
        else:
            self.tournaments_table.insert(tournament.serialize())

    def get_all_tournaments(self):
        """Récupère tous les tournois de la base de données."""
        return self.tournaments_table.all()

    def close(self):
        """Ferme la connexion à la base de données."""
        self.db.close()
