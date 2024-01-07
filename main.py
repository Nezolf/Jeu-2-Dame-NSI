import src.Game as Game

# Initialiser un plateau avec les dispositions de pions de base
Board = [
    [0,-1,0,-1,0,-1,0,-1,0,-1],
    [-1,0,-1,0,-1,0,-1,0,-1,0],
    [0,-1,0,-1,0,-1,0,-1,0,-1],
    [-1,0,-1,0,-1,0,-1,0,-1,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,1,0,1,0,1,0,1,0,1],
    [1,0,1,0,1,0,1,0,1,0],
    [0,1,0,1,0,1,0,1,0,1],
    [1,0,1,0,1,0,1,0,1,0]
]

# Variable qui dit quel joueur doit jouer le coup
player_who_plays = Game.FIRST_PLAYER_TO_PLAY


while True:
    # Afficher le plateau
    Game.print_board(Board)

    # Faire selectionner un pion au joueur
    pawn_position = Game.select_pawn(Board, player_who_plays)

    # Afficher la pré-visualisation du coup
    board_preview, moves = Game.print_move_preview(Board, pawn_position, player_who_plays)

    # Jouer le coup choisis par le joueur
    Board = Game.play_move(board_preview, Board, pawn_position, player_who_plays, moves)

    # Passer au tour de l'autre joueur
    player_who_plays *= -1