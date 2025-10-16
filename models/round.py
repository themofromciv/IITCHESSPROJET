"""Modèle pour représenter un tour de tournoi."""
from datetime import datetime


class Round:
    """Classe représentant un tour dans un tournoi."""

    def __init__(self, name):
        """
        Initialise un nouveau tour.
        Args:
            name (str): Nom du tour (ex: "Round 1")
        """
        self.name = name
        self.matches = []
        self.start_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        self.end_time = None

    def add_match(self, match):
        """
        Ajoute un match au tour.
        Args:
            match: Instance de Match à ajouter
        """
        self.matches.append(match)

    def mark_as_complete(self):
        """Marque le tour comme terminé en enregistrant l'heure de fin."""
        self.end_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    def serialize(self):
        """
        Convertit le tour en dictionnaire pour la sauvegarde.
        Returns:
            dict: Dictionnaire contenant toutes les données du tour
        """
        return {
            'name': self.name,
            'start_time': self.start_time,
            'end_time': self.end_time,
            'matches': [match.to_tuple() for match in self.matches]
        }

    def __str__(self):
        """Représentation textuelle du tour."""
        status = "Terminé" if self.end_time else "En cours"
        return f"{self.name} - {status} ({len(self.matches)} matchs)"
