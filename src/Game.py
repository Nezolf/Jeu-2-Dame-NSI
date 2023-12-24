# Définir quel joueur commence à jouer (1 -> les blancs ; -1 -> les noirs)
FIRST_PLAYER_TO_PLAY = 1

# Dictionnaire pour transphormer l'id d'une pièce sur le plateau en un caractère à afficher
PAWNS_CHARS = {
    0: " ",
    1: "█",
    -1: "▒",
    2: "#",
    -2: "#"
}


def print_board(board):
    """
    Afficher de manière textuel le plateau de jeu dans la console
    :param board: list, plateau de jeu
    :return: None
    """
    for y in range(len(board)):
        for x in range(len(board[y])):
            print(PAWNS_CHARS[board[y][x]], end=" ")
        print(y)
    print("A B C D E F G H I J")


# DEF -> Selection du pion
    # Demander un entrée comme ceci -> "Selectionner un pion >> "
        # - Transformer l'input au format "E4" en coordonées sur le plateau
        # - Vérifier que les coordonées donné sont bien celle d'un pion du joueur
        # - Renvoyer les coordonées valide du pion


# DEF -> Mouvement du pion
    # Demander où le pion doit se déplacer
        # - Transformer l'input au format "E4" en coordonées sur le plateau
        # - Verifier que le pion peut accéder au coordonées donné
        # - Verifier si il n'est pas possible que le jouer ne doit pas jouer autre chose (prise de pion est obligatoire si elle est possible)
    # Déplacer le pion sur le plateau 
