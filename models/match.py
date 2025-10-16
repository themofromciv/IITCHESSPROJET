"""Modèle pour représenter un match d'échecs."""


class Match:
    """Classe représentant un match entre deux joueurs."""

    def __init__(self, player1, player2):
        """
        Initialise un nouveau match.
        Args:
            player1: Premier joueur (instance de Player)
            player2: Deuxième joueur (instance de Player)
        """
        self.player1 = player1
        self.player2 = player2
        self.score1 = 0
        self.score2 = 0

    def set_result(self, score1, score2):
        """
    Définit le résultat du match.
        Args:
            score1 (float): Score du joueur 1 (0, 0.5, ou 1)
            score2 (float): Score du joueur 2 (0, 0.5, ou 1)
        """
        self.score1 = score1
        self.score2 = score2
        self.player1.tournament_score += score1
        self.player2.tournament_score += score2

    def to_tuple(self):
        """
        Convertit le match en tuple selon les spécifications.
    Format: ([player1, score1], [player2, score2])
        Returns:
            tuple: Représentation du match en tuple
        """
        return ([self.player1, self.score1], [self.player2, self.score2])

    def __str__(self):
        """Représentation textuelle du match."""
        return f"{self.player1.first_name} {self.player1.last_name} ({self.score1}) vs " \
            f"{self.player2.first_name} {self.player2.last_name} ({self.score2})"
