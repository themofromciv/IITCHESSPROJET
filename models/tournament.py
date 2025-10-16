"""Modèle pour représenter un tournoi d'échecs."""
from models.round import Round
from models.match import Match


class Tournament:
    """Classe représentant un tournoi d'échecs selon le système suisse."""

    def __init__(self, name, location, start_date, end_date, description=""):
        """
        Initialise un nouveau tournoi.
        Args:
            name (str): Nom du tournoi
            location (str): Lieu du tournoi
            start_date (str): Date de début (format: JJ/MM/AAAA)
            end_date (str): Date de fin (format: JJ/MM/AAAA)
            description (str): Description optionnelle du tournoi
        """
        self.name = name
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        self.description = description
        self.number_of_rounds = 4
        self.rounds = []
        self.players = []
        self.current_round = 0

    def add_player(self, player):
        """
        Ajoute un joueur au tournoi.
        Args:
            player: Instance de Player à ajouter

        Returns:
            bool: True si ajouté avec succès, False si le tournoi est plein
        """
        if len(self.players) < 8:
            player.tournament_score = 0
            self.players.append(player)
            return True
        return False

    def generate_first_round_pairs(self):
        """
        Génère les paires du premier tour.
        Les joueurs sont triés par classement, puis divisés en deux moitiés.
        """
        sorted_players = sorted(self.players, key=lambda p: p.ranking, reverse=True)
        mid = len(sorted_players) // 2
        top_half = sorted_players[:mid]
        bottom_half = sorted_players[mid:]
        round1 = Round("Round 1")
        for i in range(mid):
            match = Match(top_half[i], bottom_half[i])
            round1.add_match(match)

        self.rounds.append(round1)
        self.current_round = 1

    def generate_next_round_pairs(self):
        """
        Génère les paires pour les tours suivants.
        Les joueurs sont triés par score, puis par classement.
        """
        sorted_players = sorted(
            self.players,
            key=lambda p: (p.tournament_score, p.ranking),
            reverse=True
        )
        round_number = len(self.rounds) + 1
        new_round = Round(f"Round {round_number}")
        paired = set()
        previous_matches = self._get_all_previous_matches()
        for i, player1 in enumerate(sorted_players):
            if player1 in paired:
                continue
            for player2 in sorted_players[i+1:]:
                if player2 in paired:
                    continue
                if not self._have_played_together(player1, player2, previous_matches):
                    match = Match(player1, player2)
                    new_round.add_match(match)
                    paired.add(player1)
                    paired.add(player2)
                    break
        self.rounds.append(new_round)
        self.current_round = round_number

    def _get_all_previous_matches(self):
        """Récupère tous les matchs des tours précédents."""
        matches = []
        for round_obj in self.rounds:
            for match in round_obj.matches:
                matches.append((match.player1, match.player2))
        return matches

    def _have_played_together(self, player1, player2, previous_matches):
        """Vérifie si deux joueurs se sont déjà affrontés."""
        for p1, p2 in previous_matches:
            if (p1 == player1 and p2 == player2) or (p1 == player2 and p2 == player1):
                return True
        return False

    def serialize(self):
        """Convertit le tournoi en dictionnaire pour la sauvegarde."""
        return {
            'name': self.name,
            'location': self.location,
            'start_date': self.start_date,
            'end_date': self.end_date,
            'description': self.description,
            'number_of_rounds': self.number_of_rounds,
            'current_round': self.current_round,
            'players': [player.serialize() for player in self.players],
            'rounds': [round_obj.serialize() for round_obj in self.rounds]
        }

    def __str__(self):
        """Représentation textuelle du tournoi."""
        return f"{self.name} - {self.location} ({self.start_date} au {self.end_date})"
