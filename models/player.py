"""Modèle pour représenter un joueur d'échecs."""


class Player:
    """Classe représentant un joueur de tournoi d'échecs."""

    def __init__(self, first_name, last_name, birth_date, gender, ranking):
        """
        Initialise un nouveau joueur.
        Args:
            first_name (str): Prénom du joueur
            last_name (str): Nom de famille du joueur
            birth_date (str): Date de naissance (format: JJ/MM/AAAA)
            gender (str): Sexe du joueur (M/F)
            ranking (int): Classement du joueur (nombre positif)
        """
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.gender = gender
        self.ranking = ranking
        self.tournament_score = 0

    def serialize(self):
        """
    Convertit l'instance en dictionnaire pour la sauvegarde.
        Returns:
            dict: Dictionnaire contenant toutes les données du joueur
        """
        return {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'birth_date': self.birth_date,
            'gender': self.gender,
            'ranking': self.ranking
        }

    @staticmethod
    def deserialize(data):
        """
    Crée une instance Player à partir d'un dictionnaire.
        Args:
            data (dict): Dictionnaire contenant les données du joueur
        Returns:
            Player: Nouvelle instance de Player
        """
        return Player(
            first_name=data['first_name'],
            last_name=data['last_name'],
            birth_date=data['birth_date'],
            gender=data['gender'],
            ranking=data['ranking']
        )

    def __str__(self):
        """Représentation textuelle du joueur."""
        return f"{self.first_name} {self.last_name} (Classement: {self.ranking})"
