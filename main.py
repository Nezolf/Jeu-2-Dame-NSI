import src.Game as Game

# Initialiser un plateau avec les dispositions de pions de base
Plateau = [
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
turn_of = Game.FIRST_PLAYER_TO_PLAY

# Afficher le plateau
Game.print_board(Plateau)

# Faire selectionner un pion au joueur
pawn_position = Game.select_pawn(Plateau, turn_of)

# Afficher la pré-visualisation du coup
Game.print_move_preview(Plateau, pawn_position, turn_of)