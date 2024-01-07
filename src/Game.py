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

        player_input = input("Selectionner un pion (ex. A3) >> ").replace(" ", "")

        try:
            if len(player_input) != 2:
                raise ValueError
                    
            c = LETTER_TO_NUM[player_input[0].upper()]
            l = int(player_input[1])

            if board[l][c] == 0: # Vérifier que la case selectionnée n'est pas vide
                print("Il n'y a pas de pion à cette position.")

            elif board[l][c] != player: # Vérifier que la case selectionnée n'est pas ocuppée par un pion de l'addversaire
                print("Ce pion ne vous appartien pas.")

            # Vérifier si le joueur ne doit pas jouer un autre coup (prise obligatoire)
            
            else:
                input_check = True # Tous les tests sont validé, la condition passe su VRAI
                
        except(KeyError, ValueError):
                print("Entrée Invalide !")

    return l, c
        

def print_move_preview(board, pawn, player):

    moves = {}

    l, c = pawn

    board_copy = copy.deepcopy(board)

    if can_take_pawn(board_copy, pawn, player):
        
        new_poss = []

        if can_take_up_left(board_copy, l, c, player):
            board_copy[l-1][c-1] = "x"
            board_copy[l-2][c-2] = "."
            new_poss.append((l-2,c-2))
            moves[f'{l-2}{c-2}'] = {"takes": []}
        
        if can_take_up_right(board_copy, l, c, player):
            board_copy[l-1][c+1] = "x"
            board_copy[l-2][c+2] = "."
            new_poss.append((l-2,c+2))
        
        if can_take_down_left(board_copy, l, c, player):
            board_copy[l+1][c-1] = "x"
            board_copy[l+2][c-2] = "."
            new_poss.append((l+2,c-2))
        
        if can_take_down_right(board_copy, l, c, player):
            board_copy[l+1][c+1] = "x"
            board_copy[l+2][c+2] = "."
            new_poss.append((l+2,c+2))

        for new_l, new_c in new_poss:
            if can_take_pawn(board_copy, (new_l, new_c), player): pass


    else:
        try:
            if board_copy[l-player][c-1] == 0:
                board_copy[l-player][c-1] = "."
                moves[f'{l-player}{c-1}'] = {'takes': []}
        except IndexError:
            pass
        
        try:
            if board_copy[l-player][c+1] == 0:
                board_copy[l-player][c+1] = "."
                moves[f'{l-player}{c+1}'] = {'takes': []}
        except IndexError:
            pass

    
    print_board(board_copy)
    return board_copy, moves


# DEF -> Mouvement du pion
    # Demander où le pion doit se déplacer
        # - Transformer l'input au format "E4" en coordonées sur le plateau
        # - Verifier que le pion peut accéder au coordonées donné
        # - Verifier si il n'est pas possible que le jouer ne doit pas jouer autre chose (prise de pion est obligatoire si elle est possible)
    # Déplacer le pion sur le plateau 

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
    for taken_pawn in moves[f'{l}{c}']['takes']:
        board_copy[taken_pawn[0]][taken_pawn[1]] = 0
    
    return board_copy
