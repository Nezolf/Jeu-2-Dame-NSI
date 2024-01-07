def can_take_up_left(board, l, c, player):
    """
    Vérifier si un pion à la possibilité de prednre un pion sur sa diagonale gauche vers le haut
    :param board: list, Plateau de jeu
    :param l: Ligne sur lequel se trouve le pion
    :param c: Colonne sur lequel se trouve le pion
    :param player: Joueur qui joue le coup
    :return: Bool, True si le pion peut prendre sinon False
    """ 

    return ((1 < l) and (1 < c)) and board[l-1][c-1] == -player and board[l-2][c-2] == 0


def can_take_up_right(board, l, c, player):
    """
    Vérifier si un pion à la possibilité de prednre un pion sur sa diagonale droite vers le haut
    :param board: list, Plateau de jeu
    :param l: Ligne sur lequel se trouve le pion
    :param c: Colonne sur lequel se trouve le pion
    :param player: Joueur qui joue le coup
    :return: Bool, True si le pion peut prendre sinon False
    """ 
    
    return ((1 < l) and (c < 8)) and board[l-1][c+1] == -player and board[l-2][c+2] == 0


def can_take_down_left(board, l, c, player):
    """
    Vérifier si un pion à la possibilité de prednre un pion sur sa diagonale gauche vers le bas
    :param board: list, Plateau de jeu
    :param l: Ligne sur lequel se trouve le pion
    :param c: Colonne sur lequel se trouve le pion
    :param player: Joueur qui joue le coup
    :return: Bool, True si le pion peut prendre sinon False
    """ 

    return ((l < 8) and (1 < c)) and board[l+1][c-1] == -player and board[l+2][c-2] == 0


def can_take_down_right(board, l, c, player):
    """
    Vérifier si un pion à la possibilité de prednre un pion sur sa diagonale droite vers le bas
    :param board: list, Plateau de jeu
    :param l: Ligne sur lequel se trouve le pion
    :param c: Colonne sur lequel se trouve le pion
    :param player: Joueur qui joue le coup
    :return: Bool, True si le pion peut prendre sinon False
    """ 
    
    return ((l < 8) and (c < 8)) and board[l+1][c+1] == -player and board[l+2][c+2] == 0


def can_take_pawn(board, pawn, player):
    """
    Fonction qui permet de savoir si un pion donné a la posibilité de prendre un pion addverse
    :param board: list, tableau représentent le plateau de jeu
    :param pawn: float, coordonées du pion sur le plateau
    :param player: int, couleur du joueur qui joue le coup
    :return: bool, True si le pion donné peut prendre un pion sinon revoie False
    """

    l, c = pawn

    diago_up_left = can_take_up_left(board, l, c, player) # Vérifier si le pion à la possibilité de prednre un pion sur sa diagonale gauche vers le haut
    diago_up_right = can_take_up_right(board, l, c, player) # Vérifier si le pion à la possibilité de prednre un pion sur sa diagonale droite vers le haut
    diago_down_left = can_take_down_left(board, l, c, player) # Vérifier si le pion à la possibilité de prednre un pion sur sa diagonale gauche vers le bas
    diago_down_right = can_take_down_right(board, l, c, player) # Vérifier si le pion à la possibilité de prednre un pion sur sa diagonale droite vers le haut

    return diago_up_left or diago_up_right or diago_down_left or diago_down_right