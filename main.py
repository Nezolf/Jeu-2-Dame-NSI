import src.Game as Game

# Initialiser un plateau avec les dispositions de pions de base
Board = Game.INITIAL_BOARD

# Afficher un texte d'introduction avec quelques règles de base
print("Bienvenue sur ce jeu de Dames !\nPour commencer à jouer, nous vous invitons à lire ces quelques règles ;\n  - Le pions blancs sont symboliser par un b, et les pions noirs par un n\n  - Le joueur qui joue en premier est toujours celui qui joue les pions blancs\n  - A chaques tours, plusieures entrée vous serons demandé, il faut sésire la case corespondent à\n    ce qui vous est demander, pour répondre, il sufit de répondre par la lettre de la colone suivit\n    du numéreau de la ligne comme ceci -> A3 ou même f7\n  - Le gagnant de la partie est décider en fonction du joueur à qui il reste des pion à la fin de la partie\n  - La fin de la partie est décidé quand un des joueur ne peux bouger\n    un de ses pions ou qu'un joueur a perdu tout ses pions\n  - Si vous avez la possibilité de prendre un pion adversse, vous avez obligation de prednre un pion")
input("\n\n si ces règles vous conviennes, vous pouvez appuyer sur [ENTER] pour lancer le jeu  ")
print("\n\n\n\n\n\n")

# Variable qui dit quel joueur doit jouer le coup
player_who_plays = Game.FIRST_PLAYER_TO_PLAY

try:
    while Game.both_player_have_pawns(Board) and Game.still_player_can_play(Board, player_who_plays):
        # Afficher le plateau
        Game.print_board(Board)

        player_turn = True

        # Faire selectionner un pion au joueur
        pawn_position = Game.select_pawn(Board, player_who_plays)

        while player_turn:
            
            # Afficher la pré-visualisation du coup
            board_preview, moves = Game.print_move_preview(Board, pawn_position, player_who_plays)

            # Jouer le coup choisis par le joueur
            Board, new_poss = Game.play_move(board_preview, Board, pawn_position, player_who_plays, moves)

            if moves[f"{new_poss[0]}{new_poss[1]}"]["take"] != None:
                if not Game.can_take_pawn(Board, new_poss, player_who_plays):
                    player_turn = False # Terminer le coup du joueur
                else:
                    Game.print_board(Board) # Afficher le plateau (pour montrer l'avancé du coup)
                    print("Vous pouvez effectuer une autre action dur ce tours")
                    pawn_position = new_poss # Mettre à jour la position du pion dans la boucle

            else: # Dire que le coup du joueur est terminé
                player_turn = False

        # Passer au tour de l'autre joueur
        player_who_plays *= -1

    # Afficher le résultat de la partie
    input("\nPartie terminée !\nAppuyez sur [ENTER] pour révéler les résultats !   ")
    winer = Game.get_winner(Board)
    if winer == 1:
        print("Victoire du joueur blanc !")
    elif winer == -1:
        print("Victoire du joueur noir !")
    else:
        print("Egalité !")

# Eviter le message d'erreur pas beau du CTRL + C
except KeyboardInterrupt:
    print("\n\nVous avez quitté le jeu.\nA très bientôt :)")