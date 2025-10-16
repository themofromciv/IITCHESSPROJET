"""Vues pour la gestion des joueurs."""


class PlayerView:
    """Classe pour afficher les informations relatives aux joueurs."""

    @staticmethod
    def get_player_info():
        """Demande les informations d'un nouveau joueur."""
        print("\n" + "-"*50)
        print("AJOUT D'UN NOUVEAU JOUEUR")
        print("-"*50)
        first_name = input("Prenom : ")
        last_name = input("Nom : ")
        birth_date = input("Date de naissance (JJ/MM/AAAA) : ")
        gender = ""
        while gender not in ['M', 'F']:
            gender = input("Sexe (M/F) : ").upper()
        ranking = 0
        while ranking <= 0:
            try:
                ranking = int(input("Classement (nombre positif) : "))
                if ranking <= 0:
                    print("Le classement doit etre un nombre positif.")
            except ValueError:
                print("Veuillez entrer un nombre valide.")
        return {
            'first_name': first_name,
            'last_name': last_name,
            'birth_date': birth_date,
            'gender': gender,
            'ranking': ranking
        }

    @staticmethod
    def display_players(players, title="LISTE DES JOUEURS"):
        """Affiche une liste de joueurs."""
        print("\n" + "="*50)
        print(title.center(50))
        print("="*50)
        if not players:
            print("\nAucun joueur enregistre.")
            return
        for i, player in enumerate(players, 1):
            print(f"\n{i}. {player.last_name} {player.first_name}")
            print(f"   Date de naissance : {player.birth_date}")
            print(f"   Sexe : {player.gender}")
            print(f"   Classement : {player.ranking}")

    @staticmethod
    def select_player(players):
        """Permet de selectionner un joueur dans une liste."""
        if not players:
            return None
        PlayerView.display_players(players)
        try:
            choice = int(input("\nNumero du joueur : "))
            if 1 <= choice <= len(players):
                return players[choice - 1]
            else:
                print("Numero invalide.")
                return None
        except ValueError:
            print("Veuillez entrer un nombre valide.")
            return None

    @staticmethod
    def get_new_ranking():
        """Demande un nouveau classement."""
        while True:
            try:
                ranking = int(input("Nouveau classement : "))
                if ranking > 0:
                    return ranking
                else:
                    print("Le classement doit etre un nombre positif.")
            except ValueError:
                print("Veuillez entrer un nombre valide.")
