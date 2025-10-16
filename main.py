"""
Application de gestion de tournois d'echecs.
Systeme suisse pour 8 joueurs avec 4 tours.
"""
from database.db_manager import DatabaseManager
from controllers.main_controller import MainController


def main():
    """Fonction principale de l'application."""
    db_manager = DatabaseManager('chess_tournament.json')
    main_controller = MainController(db_manager)
    main_controller.run()


if __name__ == "__main__":
    main(),
