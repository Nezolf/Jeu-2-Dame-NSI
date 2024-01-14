import copy
from src.Check_Takes import *

# Définir quel joueur commence à jouer (1 -> les blancs ; -1 -> les noirs)
FIRST_PLAYER_TO_PLAY = 1

# Dictionnaire pour transphormer l'id d'une pièce sur le plateau en un caractère à afficher
PAWNS_CHARS = {
    0: " ",   # Case vide
    1: "b",   # Pion blanc
    -1: "n",  # Pion noir
    2: "B",   # Dame blanche
    -2: "N",  # Dame noire
    ".": "*", # Prévisualisation
    "x": "X", # Pion pris par un coup
}

# Dictionnaire pour pouvoir transformer les coordonées de collone sur le plateau en index
LETTER_TO_NUM = {
        "A": 0,
        "B": 1,
        "C": 2,
        "D": 3,
        "E": 4,
        "F": 5,
        "G": 6,
        "H": 7,
        "I": 8,
        "J": 9
}

INITIAL_BOARD = [
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


def both_player_have_pawns(board):
    """
    Vérifier que tous les joueurs ont au moins 1 pion
    :param board: list, plateau de jeux
    :return: bool, True si les deux joueurs on au moins 1 pion, sinon False
    """

    white_pawn_count = 0
    black_pawn_count = 0

    for l in range(10):
        for c in range(10):
            
            if board[l][c] == 1:
                white_pawn_count += 1
            elif board[l][c] == -1:
                black_pawn_count += 1
    
    return white_pawn_count > 0 and black_pawn_count > 0


def still_player_can_play(board, player):
    """
    Vérifier qu'un joueur à la possibilité de jouer
    :param board: list, plateau de jeux
    :param player: int, joueur qui est en train de jouer
    :return: bool, True si le joueur peux jouer un coup, sinon False
    """

    player_can_play = False

    for l in range(10):
        for c in range(10):
            if board[l][c] == player and can_move(board, l, c, board[l][c]):
                player_can_play = True
    
    return player_can_play


def get_winner(board):
    """
    Retourner le numéreau du joueur qui à gagné la partie
    :param board: list, plateau de jeux
    :return: int, 1 si le vainqueure est le joueur blanc, -1 si c'est le joueur noir et 0 si il y a égalité
    """
    
    white_pawn_count = 0
    black_pawn_count = 0

    for l in range(10):
        for c in range(10):
            if board[l][c] in [1, 2]:
                white_pawn_count += 1
            elif board[l][c] in [-1, -2]:
                black_pawn_count += 1
    
    if white_pawn_count > black_pawn_count:
        return 1
    elif black_pawn_count > white_pawn_count:
        return -1
    else:
        return 0


def print_board(board):
    """
    Afficher de manière textuel le plateau de jeu dans la console
    :param board: list, plateau de jeu
    :return: None
    """
    for l in range(len(board)):
        for c in range(len(board[l])):
            print(PAWNS_CHARS[board[l][c]], end=" ")
        print(f" {l}")
    print("A B C D E F G H I J")
    

def select_pawn(board, player):
    """
    Demande au joueur le pion qu'il souhaite jouer et retourne les coordonées utilisable du pion
    :param board: list, plateau de jeu
    :param player: int, identifient du joueur qui est en train de jouer le coup
    :return: tuple, coordonées du pion selectionné
    """

    input_check = False # <- FAUX tant que l'entrée du joueur n'est pas vérifiée
                                # C'est à dire :
                                    # - l'entrée donné corespond bien à des coordonées sur le plateau
                                    # - les coordonées corespondes bien à un pion existant et qui appartient au joueur
                                    # - le pion choisis PEUT être jouer (pas d'obligation de jouer un autre pion)
    
    while not input_check:

        player_color = "blanc" if player == 1 else "noir"
        player_input = input(f"Joueur {player_color}, selectionnez un pion (ex. A3) >> ").replace(" ", "")

        try:
            if len(player_input) != 2:
                raise ValueError
                    
            c = LETTER_TO_NUM[player_input[0].upper()]
            l = int(player_input[1])

            # Faire la liste de tous les pions du joueur qui peuvent en prendre un autre
            players_can_take_pawns = []
            for verif_line in range(10):
                for verif_col in range(10):
                    if board[verif_line][verif_col] == player and can_take_pawn(board, (verif_line, verif_col), player):
                        players_can_take_pawns.append(f"{verif_line}{verif_col}")

            if board[l][c] == 0: # Vérifier que la case selectionnée n'est pas vide
                print("Il n'y a pas de pion à cette position.")

            elif board[l][c] != player: # Vérifier que la case selectionnée n'est pas ocuppée par un pion de l'addversaire
                print("Ce pion ne vous appartien pas.")

            elif not can_move(board, l, c, player): # Vérifier que le pion selectionner peux se déplacer
                print("Ce pion n'a aucune action possible")
            
            elif (not (f"{l}{c}" in players_can_take_pawns)) and (len(players_can_take_pawns) != 0): # Vérifier que le joueur n'essaye pas de jouer un pion qui n'a pas le droit de jouer
                print("Vous n'avez pas le droit de jouer ce pion (vous êtes obliger de prendre dès que vous le pouvez)")

            else:
                input_check = True # Tous les tests sont validé, la condition passe su VRAI
                
        except(KeyError, ValueError):
                print("Entrée Invalide !")

    return l, c


def print_move_preview(board, pawn, player): # /!\ GERER LES PRISES A LA SUITE !
    """
    DOC STRING HERE
    """

    moves = {} # f"{new_l}{new_c}": {"init-pos": (l, c), "final_pos": (new_l, new_c), "take": (l, c)}

    l, c = pawn

    board_copy = copy.deepcopy(board)

    if can_take_pawn(board_copy, pawn, player):

        if can_take_up_left(board_copy, l, c, player):
            board_copy[l-1][c-1] = "x"
            board_copy[l-2][c-2] = "."
            moves[f'{l-2}{c-2}'] = {"init-pos": (l, c), "final_pos": (l-2, c-2), "take": (l-1, c-1)}
        
        if can_take_up_right(board_copy, l, c, player):
            board_copy[l-1][c+1] = "x"
            board_copy[l-2][c+2] = "."
            moves[f'{l-2}{c+2}'] = {"init-pos": (l, c), "final_pos": (l-2, c+2), "take": (l-1, c+1)}
        
        if can_take_down_left(board_copy, l, c, player):
            board_copy[l+1][c-1] = "x"
            board_copy[l+2][c-2] = "."
            moves[f'{l+2}{c-2}'] = {"init-pos": (l, c), "final_pos": (l+2, c-2), "take": (l+1, c-1)}
        
        if can_take_down_right(board_copy, l, c, player):
            board_copy[l+1][c+1] = "x"
            board_copy[l+2][c+2] = "."
            moves[f'{l+2}{c+2}'] = {"init-pos": (l, c), "final_pos": (l+2, c+2), "take": (l+1, c+1)}

    else:
        try:
            if board_copy[l-player][c-1] == 0:
                board_copy[l-player][c-1] = "."
                moves[f'{l-player}{c-1}'] = {"init-pos": (l, c), "final_pos": (l-player, c-1), "take": None}
        except IndexError:
            pass
        
        try:
            if board_copy[l-player][c+1] == 0:
                board_copy[l-player][c+1] = "."
                moves[f'{l-player}{c+1}'] = {"init-pos": (l, c), "final_pos": (l-player, c+1), "take": None}
        except IndexError:
            pass

    
    print_board(board_copy)
    return board_copy, moves


def play_move(board_preview, board, pawn, player, moves): 
    """
    Jouer le coup choisis par le joueur et retourner le plateau modifié
    :param board_preview: list, plateau de jeu
    :param pawn: tuple, coordonées du pion à jouer
    :param player: joueur qui joue le coup
    :return: list, list, plateau de jeu actualisé en fonction du coup joué
    """

    input_check = False # <- FAUX tant que l'entrée du joueur n'est pas vérifiée
                                # C'est à dire :
                                    # - l'entrée donné corespond bien à des coordonées sur le plateau
                                    # - les coordonées corespondes bien à un coup jouable par le joueur
    
    while not input_check:

        player_input = input("Où voulez vous déplacer ce pion ? (ex. A3) >> ").replace(" ", "")

        try:

            if len(player_input) != 2:
                raise ValueError
                    
            c = LETTER_TO_NUM[player_input[0].upper()]
            l = int(player_input[1])

            if board_preview[l][c] != ".": # Vérifier que le coup selectionnée est jouable
                print("Il n'y a pas de coup jouable à cette position.")         
            else:
                input_check = True # Tous les tests sont validé, la condition passe sur VRAI
                
        except(KeyError, ValueError):
                print("Entrée Invalide !")
    
    board_copy = copy.deepcopy(board) # Copie du tableau pour pouvoir le modifier sans modifier tout de suite le vrai plateau de jeu

    # Déplacer le pion joué
    board_copy[l][c] = player # Placer le pion à sa position finale
    board_copy[pawn[0]][pawn[1]] = 0 # Retirer le pion de sa position initiale

    # Retirer les pions "mangé"
    taken_pawn = moves[f"{l}{c}"]["take"]
    if taken_pawn != None:
        board_copy[taken_pawn[0]][taken_pawn[1]] = 0
       
    return board_copy, (l, c)