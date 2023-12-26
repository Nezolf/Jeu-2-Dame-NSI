import copy

# Définir quel joueur commence à jouer (1 -> les blancs ; -1 -> les noirs)
FIRST_PLAYER_TO_PLAY = 1

# Dictionnaire pour transphormer l'id d'une pièce sur le plateau en un caractère à afficher
PAWNS_CHARS = {
    0: " ",   # Case vide
    1: "█",   # Pion blanc
    -1: "▒",  # Pion noir
    2: "#",   # Dame blanche
    -2: "#",  # Dame noire
    ".": "•", # Prévisualisation
    "x": "X", # Pion pris dans le déplacement
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

    letter_to_num = {
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

    input_check = False
    while not input_check:
        player_input = input("Selectionner un pion (ex. A3) >> ").replace(" ", "")

        try:
            if len(player_input) != 2:
                raise ValueError
                    
            c = letter_to_num[player_input[0].upper()]
            l = int(player_input[1])

            if board[l][c] == 0:
                print("Il n'y a pas de pion à cette position.")
            elif board[l][c] != player:
                print("Ce pion ne vous appartien pas.")

            # Vérifier si le joueur ne doit pas jouer un autre coup (prise obligatoire)
            
            else:
                input_check = True
                
        except(KeyError, ValueError):
                print("Entrée Invalide !")

    return l, c
        

def print_move_preview(board, pawn, player):
    """
    Afficher le plateau avec l'appersus des coups possible avec le pion selectionné
    :param board: list, plateau de jeu    
    :param pawn: tuple, coordonées du pion à jouer
    :return: None
    """

    board_copy = copy.deepcopy(board)

    l, c = pawn

    direction_movement = player * -1
    
    if c == 0 and board_copy[l + direction_movement][c+1] == 0:
        board_copy[l + direction_movement][c+1] = "."

    elif c == 9 and board_copy[l + direction_movement][c-1] == 0:
        board_copy[l + direction_movement][c-1] = "."

    elif 0 < c < 9 and board_copy[l + direction_movement][c-1] == 0 and board_copy[l + direction_movement][c+1] == 0:
        board_copy[l + direction_movement][c-1] = "."
        board_copy[l + direction_movement][c+1] = "."
     
    print_board(board_copy)


# DEF -> Mouvement du pion
    # Demander où le pion doit se déplacer
        # - Transformer l'input au format "E4" en coordonées sur le plateau
        # - Verifier que le pion peut accéder au coordonées donné
        # - Verifier si il n'est pas possible que le jouer ne doit pas jouer autre chose (prise de pion est obligatoire si elle est possible)
    # Déplacer le pion sur le plateau 

