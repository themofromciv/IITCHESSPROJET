"""Vue principale de l'application."""


class MainView:
    """Classe pour afficher le menu principal."""

    def display_main_menu():
        """Affiche le menu principal et retourne le choix de l'utilisateur."""
        print("\n" + "=" * 50)
        print("GESTIONNAIRE DE TOURNOIS D'ECHECS".center(50))
        print("="*50)
        print("\n1. Gestion des joueurs")
        print("2. Gestion des tournois")
        print("3. Rapports")
        print("4. Quitter")
        print("\n" + "-" * 50)
        choice = input("Votre choix : ")
        return choice

    def display_player_menu():
        """Affiche le menu de gestion des joueurs."""
        print("\n" + "="*50)
        print("GESTION DES JOUEURS".center(50))
        print("="*50)
        print("\n1. Ajouter un joueur")
        print("2. Modifier le classement d'un joueur")
        print("3. Voir tous les joueurs")
        print("4. Retour au menu principal")
        print("\n" + "-" * 50)
        choice = input("Votre choix : ")
        return choice

    def display_tournament_menu():
        """Affiche le menu de gestion des tournois."""
        print("\n" + "=" * 50)
        print("GESTION DES TOURNOIS".center(50))
        print("="*50)
        print("\n1. Creer un nouveau tournoi")
        print("2. Reprendre un tournoi en cours")
        print("3. Voir tous les tournois")
        print("4. Retour au menu principal")
        print("\n" + "-" * 50)
        choice = input("Votre choix : ")
        return choice

    @staticmethod
    def display_reports_menu():
        """Affiche le menu des rapports."""
        print("\n" + "=" * 50)
        print("RAPPORTS".center(50))
        print("="*50)
        print("\n1. Liste de tous les joueurs (par ordre alphabetique)")
        print("2. Liste de tous les joueurs (par classement)")
        print("3. Liste de tous les tournois")
        print("4. Details d'un tournoi")
        print("5. Retour au menu principal")
        print("\n" + "-" * 50)
        choice = input("Votre choix : ")
        return choice

    def display_message(message):
        """Affiche un message à l'utilisateur."""
        print(f"\n>>> {message}")

    def display_error(error):
        """Affiche un message d'erreur."""
        print(f"\n!!! ERREUR : {error}")

    def pause():
        """Met en pause et attend que l'utilisateur appuie sur Entree."""
        input("\nAppuyez sur Entree pour continuer...")
