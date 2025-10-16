"""Vues pour la gestion des tournois."""


class TournamentView:
    """Classe pour afficher les informations relatives aux tournois."""

    @staticmethod
    def get_tournament_info():
        """Demande les informations d'un nouveau tournoi."""
        print("\n" + "-"*50)
        print("CREATION D'UN NOUVEAU TOURNOI")
        print("-"*50)
        name = input("Nom du tournoi : ")
        location = input("Lieu : ")
        start_date = input("Date de debut (JJ/MM/AAAA) : ")
        end_date = input("Date de fin (JJ/MM/AAAA) : ")
        description = input("Description (optionnel) : ")
        return {
            'name': name,
            'location': location,
            'start_date': start_date,
            'end_date': end_date,
            'description': description
        }

    @staticmethod
    def display_tournaments(tournaments):
        """Affiche une liste de tournois."""
        print("\n" + "="*50)
        print("LISTE DES TOURNOIS".center(50))
        print("="*50)
        if not tournaments:
            print("\nAucun tournoi enregistre.")
            return
        for i, tournament in enumerate(tournaments, 1):
            print(f"\n{i}. {tournament['name']}")
            print(f"   Lieu : {tournament['location']}")
            print(f"   Dates : {tournament['start_date']} au {tournament['end_date']}")
            print(f"   Tours : {tournament['current_round']}/{tournament['number_of_rounds']}")
            print(f"   Joueurs : {len(tournament['players'])}")

    @staticmethod
    def display_tournament_details(tournament):
        """Affiche les details complets d'un tournoi."""
        print("\n" + "="*50)
        print(f"TOURNOI : {tournament['name']}".center(50))
        print("="*50)
        print(f"\nLieu : {tournament['location']}")
        print(f"Dates : {tournament['start_date']} au {tournament['end_date']}")
        print(f"Description : {tournament['description']}")
        print(f"Tours : {tournament['current_round']}/{tournament['number_of_rounds']}")
        print("\n" + "-"*50)
        print("JOUEURS INSCRITS")
        print("-"*50)
        for i, player in enumerate(tournament['players'], 1):
            print(f"{i}. {player['last_name']} {player['first_name']} (Classement: {player['ranking']})")
        if tournament['rounds']:
            print("\n" + "-"*50)
            print("TOURS")
            print("-"*50)
            for round_data in tournament['rounds']:
                print(f"\n{round_data['name']}")
                print(f"Debut : {round_data['start_time']}")
                if round_data['end_time']:
                    print(f"Fin : {round_data['end_time']}")
                else:
                    print("Statut : En cours")
                print("\nMatchs :")
                for match in round_data['matches']:
                    player1_data, score1 = match[0]
                    player2_data, score2 = match[1]
                    print(f"  {player1_data['first_name']} {player1_data['last_name']} ({score1}) vs "
                          f"{player2_data['first_name']} {player2_data['last_name']} ({score2})")

    @staticmethod
    def display_round_matches(round_obj):
        """Affiche les matchs d'un tour."""
        print("\n" + "="*50)
        print(f"{round_obj.name}".center(50))
        print("="*50)
        for i, match in enumerate(round_obj.matches, 1):
            print(f"\nMatch {i}:")
            print(f"  {match.player1.first_name} {match.player1.last_name} (Classement: {match.player1.ranking})")
            print(f"  {match.player2.first_name} {match.player2.last_name} (Classement: {match.player2.ranking})")

    @staticmethod
    def get_match_result():
        """Demande le resultat d'un match."""
        print("\nResultat du match :")
        print("1. Victoire du joueur 1")
        print("2. Victoire du joueur 2")
        print("3. Match nul")
        while True:
            choice = input("Votre choix : ")
            if choice == '1':
                return (1.0, 0.0)
            elif choice == '2':
                return (0.0, 1.0)
            elif choice == '3':
                return (0.5, 0.5)
            else:
                print("Choix invalide. Veuillez choisir 1, 2 ou 3.")

    @staticmethod
    def display_tournament_standings(players):
        """Affiche le classement du tournoi."""
        print("\n" + "="*50)
        print("CLASSEMENT DU TOURNOI".center(50))
        print("="*50)
        sorted_players = sorted(players, key=lambda p: p.tournament_score, reverse=True)
        for i, player in enumerate(sorted_players, 1):
            print(f"{i}. {player.last_name} {player.first_name} - {player.tournament_score} points")

    @staticmethod
    def select_tournament(tournaments):
        """Permet de selectionner un tournoi dans une liste."""
        if not tournaments:
            return None
        TournamentView.display_tournaments(tournaments)
        try:
            choice = int(input("\nNumero du tournoi : "))
            if 1 <= choice <= len(tournaments):
                return tournaments[choice - 1]
            else:
                print("Numero invalide.")
                return None
        except ValueError:
            print("Veuillez entrer un nombre valide.")
            return None
