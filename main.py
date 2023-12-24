import src.Game as Game

# Initialiser un plateau avec les dispositions de pions de base
PLATEAU = [
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
Game.print_board(PLATEAU)

pawn_position = Game.select_pawn(PLATEAU, turn_of)