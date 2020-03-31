# Author: Alex Shin
# Date: March 12, 2020
# Description: Program that simulates the Xiangqi game with XiangqiGame class, a parent Piece class and subclasses for
#              each of the seven game pieces that inherit from the Piece class. The classes interact with each other to
#              initialize a game board with piece objects on them, and is able to keep track of and execute making moves
#              on the board according to appropriate rules and requirements of the game and the individual pieces.

class XiangqiGame:
    """
    Represents a Xiangqi game with data members to initialize the game board, game pieces on the board in their starting
    positions, list of pieces on/off the board for each player, game state, turns, and check status for both players.
    Includes methods to print and get board, get and set game status, get and set turns, get and set check status, make
    moves, and methods to evaluate valid moves, checks, checkmates and stalemates. 
    """
    def __init__(self):
        """
        Returns a game board with initial game pieces, list of pieces on/off the board, game status as unfinished,
        red player having initial turn, and with both players' check status as False.
        """

        # creates a game board with algebraic notation labels for rows and columns
        self._board = [
            ['    a', ' b', ' c', ' d', ' e', ' f', ' g', ' h', ' i'],
            ['1 ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
            ['2 ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
            ['3 ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
            ['4 ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
            ['5 ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
            ['6 ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
            ['7 ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
            ['8 ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
            ['9 ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
            ['10', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ']
        ]

        # creates object instances of individual piece classes and place them on the game board for both players
        # with piece data members holding its type, location and player it belongs to
        rc1 = Chariot(Chariot, (1, 1), "red")
        self._board[1][1] = rc1

        rh1 = Horse(Horse, (1, 2), "red")
        self._board[1][2] = rh1

        re1 = Elephant(Elephant, (1, 3), "red")
        self._board[1][3] = re1

        ra1 = Adviser(Adviser, (1, 4), "red")
        self._board[1][4] = ra1

        rg = General(General, (1, 5), "red")
        self._board[1][5] = rg

        ra2 = Adviser(Adviser, (1, 6), "red")
        self._board[1][6] = ra2

        re2 = Elephant(Elephant, (1, 7), "red")
        self._board[1][7] = re2

        rh2 = Horse(Horse, (1, 8), "red")
        self._board[1][8] = rh2

        rc2 = Chariot(Chariot, (1, 9), "red")
        self._board[1][9] = rc2

        rn1 = Cannon(Cannon, (3, 2), "red")
        self._board[3][2] = rn1

        rn2 = Cannon(Cannon, (3, 8), "red")
        self._board[3][8] = rn2

        rs1 = Solider(Solider, (4, 1), "red")
        rs2 = Solider(Solider, (4, 3), "red")
        rs3 = Solider(Solider, (4, 5), "red")
        rs4 = Solider(Solider, (4, 7), "red")
        rs5 = Solider(Solider, (4, 9), "red")

        self._board[4][1] = rs1
        self._board[4][3] = rs2
        self._board[4][5] = rs3
        self._board[4][7] = rs4
        self._board[4][9] = rs5

        bs1 = Solider(Solider, (7, 1), "black")
        bs2 = Solider(Solider, (7, 3), "black")
        bs3 = Solider(Solider, (7, 5), "black")
        bs4 = Solider(Solider, (7, 7), "black")
        bs5 = Solider(Solider, (7, 9), "black")

        self._board[7][1] = bs1
        self._board[7][3] = bs2
        self._board[7][5] = bs3
        self._board[7][7] = bs4
        self._board[7][9] = bs5

        bn1 = Cannon(Cannon, (8, 2), "black")
        bn2 = Cannon(Cannon, (8, 8), "black")

        self._board[8][2] = bn1
        self._board[8][8] = bn2

        bc1 = Chariot(Chariot, (10, 1), "black")
        bh1 = Horse(Horse, (10, 2), "black")
        be1 = Elephant(Elephant, (10, 3), "black")
        ba1 = Adviser(Adviser, (10, 4), "black")
        bg = General(General, (10, 5), "black")
        ba2 = Adviser(Adviser, (10, 6), "black")
        be2 = Elephant(Elephant, (10, 7), "black")
        bh2 = Horse(Horse, (10, 8), "black")
        bc2 = Chariot(Chariot, (10, 9), "black")

        self._board[10][1] = bc1
        self._board[10][2] = bh1
        self._board[10][3] = be1
        self._board[10][4] = ba1
        self._board[10][5] = bg
        self._board[10][6] = ba2
        self._board[10][7] = be2
        self._board[10][8] = bh2
        self._board[10][9] = bc2

        # initialize list for pieces on and off the board to keep track of pieces accordingly
        self._red_on_board = [rc1, rh1, re1, ra1, rg, ra2, re2, rh2, rc2, rn1, rn2, rs1, rs2, rs3, rs4, rs5]
        self._black_on_board = [bc1, bh1, be1, ba1, bg, ba2, be2, bh2, bc2, bn1, bn2, bs1, bs2, bs3, bs4, bs5]
        self._red_removed = []
        self._black_removed = []

        # set initial game state to unfinished, initial turn to red player, and check status as False for both players
        self._game_state = "UNFINISHED"
        self._turn = "red"
        self._red_check_status = False
        self._black_check_status = False

    def get_board(self):
        """Prints the game board"""
        print(' '.join(self._board[0]))
        for i in range(1, 6):
            for j in range(len(self._board[i])):
                print(self._board[i][j], end=" ")
            print()
        print("\033[1;34m|||||||||||||||||||||||||||||\033[0m")
        for j in range(6, 11):
            for k in range(len(self._board[j])):
                print(self._board[j][k], end=" ")
            print()

    def board(self):
        """Returns the game board itself"""
        return self._board

    def get_game_state(self):
        """Returns the game state"""
        return self._game_state

    def set_game_state(self, game_state):
        """Sets the game state with the game state as parameter"""
        self._game_state = game_state

    def get_turn(self):
        """Returns player with current turn"""
        return self._turn

    def set_turn(self, player):
        """Sets the turn for player as given parameter"""
        self._turn = player

    def is_in_check(self, player):
        """Returns if given player is in check"""
        if player == 'red':
            return self._red_check_status
        elif player == 'black':
            return self._black_check_status

    def set_is_in_check(self, player, status):
        """Sets the player's check status"""
        if player == 'red':
            self._red_check_status = status
        if player == 'black':
            self._black_check_status = status

    def make_move(self, from_square, to_square):
        """Makes move with given algebraically-notated from and to locations on the board"""

        # translates given parameter for location of the piece to be moved
        row_from = int(from_square[1:])
        column_from = int(ord(from_square[0]) - 96)
        from_piece = self.board()[row_from][column_from]

        # translates given parameter for location of the board for the piece to be moved to
        row_to = int(to_square[1:])
        column_to = int(ord(to_square[0]) - 96)
        to_piece = self.board()[row_to][column_to]

        # if the location of the piece that needs to be moved is empty, return False
        if self.board()[row_from][column_from] == '  ':
            return False

        # if the piece to be moved does not belong to the player with turn, return False
        if self.get_turn() != self.board()[row_from][column_from].get_player():
            return False

        # call the checker function in the Piece class to check for rules for all pieces and individual pieces
        if Piece().checker(self._board, row_from, column_from, row_to, column_to) is True:

            # if the move is allowed, and the destination has a game piece, remove the piece from the list of pieces of
            # respective player and add to the list of removed pieces for the player
            if self.board()[row_to][column_to] != '  ':
                if self.get_turn() == "red":
                    self._black_on_board.remove(self.board()[row_to][column_to])
                    self._black_removed.append(self.board()[row_to][column_to])

                if self.get_turn() == "black":
                    self._red_on_board.remove(self.board()[row_to][column_to])
                    self._red_removed.append(self.board()[row_to][column_to])

            # place piece in the destination square
            self.board()[row_to][column_to] = self.board()[row_from][column_from]

            # empty the moved piece's former location
            self.board()[row_from][column_from] = '  '

            # set the moved piece's location accordingly
            self.board()[row_to][column_to].set_location((row_to, column_to))

            # calls check_in_check method to check if the move is allowed
            if self.check_in_check() is True:

                # if the move is allowed, check if the move puts the opposing player in check
                if self.check_put_in_check() is True:

                    # if the opposing player is in check, say so
                    if self.get_turn() == "red":
                        print("You are in check, black!")
                        self.set_is_in_check("black", True)
                    if self.get_turn() == "black":
                        print("You are in check, red!")
                        self.set_is_in_check("red", True)

                    # check if the opposing player is in checkmate
                    if self.check_or_stale() is True:
                        if self.get_turn() == "red":
                            print("Checkmate! Red wins!")
                        if self.get_turn() == "black":
                            print("Checkmate! Black wins!")
                        return True

                    return True

                # if the move does not put the opposing player in check, reset check status for players
                else:
                    if self.get_turn() == "black":
                        self.set_is_in_check("black", False)
                    if self.get_turn() == "red":
                        self.set_is_in_check("red", False)

                    # check if the opposing player is in stalemate
                    if self.check_or_stale() is True:
                        if self.get_turn() == "red":
                            print("You are stuck in a stalemate, black!")
                        if self.get_turn() == "black":
                            print("You are stuck in a stalemate, red!")
                        return True
                    return True

            # if the move is not allowed, say so, and reverse the move
            else:
                if self.get_turn() == "red":
                    print("You put yourself in check, red!")
                if self.get_turn() == "black":
                    print("You put yourself in check, black!")

                # reverse the placement of pieces
                self.board()[row_from][column_from] = from_piece
                self.board()[row_to][column_to] = to_piece

                # reinstate lists of pieces for either player
                if to_piece != '  ':
                    if self.get_turn() == "red":
                        self._black_on_board.append(to_piece)
                        self._black_removed.remove(to_piece)
                    if self.get_turn() == "black":
                        self._red_on_board.append(to_piece)
                        self._red_removed.remove(to_piece)

                # reset location of moved piece
                self.board()[row_from][column_from].set_location((row_from, column_from))

            return False
        return False

    def check_in_check(self):
        """
        Checks if the move is allowed by checking whether the move puts the player making the move in check,
        including the flying general situation. If the move is allowed, return True. Return False otherwise.
        """

        # if red player made the move, iterate over corresponding rows/columns to find red's general's location
        if self.get_turn() == "red":
            target = None
            for row in range(1, 4):
                for column in range(4, 7):
                    if self.board()[row][column] != '  ' and self.board()[row][column].get_piece_type() == General:
                        # target variable holds red's general's location
                        target = (row, column)

            # iterate over the pieces belonging to black player that is on the game board to check if any can
            # capture red's general
            poss_moves = []
            for piece in self._black_on_board:
                row_from = piece.get_location()[0]
                column_from = piece.get_location()[1]

                # store all possible moves by the black pieces on the game board into the list
                for row in range(1, 11):
                    for column in range(1, 10):
                        if Piece().checker(self._board, row_from, column_from, row, column) is True:
                            poss_moves.append((row, column))

            # if the red's general can be captured, say so, and return False to disallow red from making an illegal move
            if target in poss_moves:
                return False

            # iterate over corresponding rows/columns to find black's general's location
            black_general = None
            for row in range(8, 11):
                for column in range(4, 7):
                    # black_general holds black general's location
                    if self.board()[row][column] != '  ' and self.board()[row][column].get_piece_type() == General:
                        black_general = (row, column)

            # iterate over game board locations between two generals to see if all of the intervening spaces are empty
            if target[1] == black_general[1]:
                x = abs(target[0] - black_general[0])
                empty_squares = 0
                for i in range(1, x):
                    if self.board()[black_general[0] - i][target[1]] == '  ':
                        empty_squares += 1

                # if all intervening squares are empty, return False to disallow red from making an illegal move
                if empty_squares == x - 1:
                    return False

            # if move is allowed, return True
            return True

        # if black player made the move, iterate over corresponding rows/columns to find black's general's location
        if self.get_turn() == "black":
            target = None
            for row in range(8, 11):
                for column in range(4, 7):
                    if self.board()[row][column] != '  ' and self.board()[row][column].get_piece_type() == General:
                        # target variable holds black general's location
                        target = (row, column)

            # iterate over the pieces belonging to red player that is on the game board to check if any can
            # capture black's general
            poss_moves = []
            for piece in self._red_on_board:
                row_from = piece.get_location()[0]
                column_from = piece.get_location()[1]

                # store all possible moves by the red pieces on the game board into the list
                for row in range(1, 11):
                    for column in range(1, 10):
                        if Piece().checker(self._board, row_from, column_from, row, column) is True:
                            poss_moves.append((row, column))

            # if the black's general can be captured, say so and return False to disallow black from making illegal move
            if target in poss_moves:
                return False

            # iterate over corresponding rows/columns to find red general's location
            red_general = None
            for row in range(1, 4):
                for column in range(4, 7):
                    if self.board()[row][column] != '  ' and self.board()[row][column].get_piece_type() == General:
                        # red_general holds red general's location
                        red_general = (row, column)

            # iterate over game board locations between two generals to see if all of the intervening spaces are empty
            if target[1] == red_general[1]:
                x = abs(target[0] - red_general[0])
                empty_squares = 0
                for i in range(1, x):
                    if self.board()[red_general[0] + i][target[1]] == '  ':
                        empty_squares += 1

                # if all intervening squares are empty, return False to disallow black from making an illegal move
                if empty_squares == x - 1:
                    return False

            # if move is allowed, return True
            return True

    def check_put_in_check(self):
        """Checks if the player making the move put the opposing player in check"""
        # if the red player made the move
        if self.get_turn() == "red":
            # get black general's position
            target = None
            for row in range(8, 11):
                for column in range(4, 7):
                    if self.board()[row][column] != '  ' and self.board()[row][column].get_piece_type() == General:
                        target = (row, column)

            # iterate over red pieces on the board to see if any can capture black general
            poss_moves = []
            for piece in self._red_on_board:
                row_from = piece.get_location()[0]
                column_from = piece.get_location()[1]

                for row in range(1, 11):
                    for column in range(1, 10):
                        if Piece().checker(self._board, row_from, column_from, row, column) is True:
                            poss_moves.append((row, column))

            # if any red piece can currently capture black's general, return True
            if target in poss_moves:
                return True
            # otherwise, return False
            return False

        # if the black player made the move
        if self.get_turn() == "black":
            target = None
            # get red general's position
            for row in range(1, 4):
                for column in range(4, 7):
                    if self.board()[row][column] != '  ' and self.board()[row][column].get_piece_type() == General:
                        target = (row, column)

            # iterate over black pieces on the board to see if any can capture red general
            poss_moves = []
            for piece in self._black_on_board:
                row_from = piece.get_location()[0]
                column_from = piece.get_location()[1]

                for row in range(1, 11):
                    for column in range(1, 10):
                        if Piece().checker(self._board, row_from, column_from, row, column) is True:
                            poss_moves.append((row, column))

            # if any black piece can currently capture red's general, return True
            if target in poss_moves:
                return True
            # otherwise, return False
            return False

    def check_or_stale(self):
        """Checks if the player making the move put the opposing player in checkmate or stalemate"""

        # if red made the move
        if self.get_turn() == "red":
            # iterate over the black pieces on the board
            for piece in self._black_on_board:
                row_from = piece.get_location()[0]
                column_from = piece.get_location()[1]
                piece_from = self.board()[row_from][column_from]

                # iterate over all squares of the game board
                for row in range(1, 11):
                    for column in range(1, 10):
                        piece_to = self.board()[row][column]

                        # whenever a move is possible to be made by the black piece, make the move if allowed
                        # in order to check if a move can be made by a black piece next turn to not be in check
                        if Piece().checker(self._board, row_from, column_from, row, column) is True:

                            if self.board()[row][column] != '  ':

                                self._red_on_board.remove(self.board()[row][column])
                                self._red_removed.append(self.board()[row][column])

                            self.board()[row][column] = self.board()[row_from][column_from]
                            self.board()[row_from][column_from] = '  '
                            self.board()[row][column].set_location((row, column))

                            # call the check_put_in_check function to check if red still has black in check
                            # if so, reverse the moves and keep iterating
                            if self.check_put_in_check() is True:

                                self.board()[row_from][column_from] = piece_from
                                self.board()[row][column] = piece_to

                                if piece_to != '  ':
                                    self._red_on_board.append(piece_to)
                                    self._red_removed.remove(piece_to)

                                self.board()[row_from][column_from].set_location((row_from, column_from))

                            # call the check_in_check function to check if black piece's move would cause the
                            # flying general situation, and if so, reverse the moves and keep iterating
                            elif self.check_in_check() is False:

                                self.board()[row_from][column_from] = piece_from
                                self.board()[row][column] = piece_to

                                if piece_to != '  ':
                                    self._red_on_board.append(piece_to)
                                    self._red_removed.remove(piece_to)

                                self.board()[row_from][column_from].set_location((row_from, column_from))

                            # if a move by a black piece causes black to not be in check, reverse the moves, set turn,
                            # and return False
                            else:
                                self.board()[row_from][column_from] = piece_from
                                self.board()[row][column] = piece_to

                                if piece_to != '  ':
                                    self._red_on_board.append(piece_to)
                                    self._red_removed.remove(piece_to)

                                self.board()[row_from][column_from].set_location((row_from, column_from))

                                self.set_turn("black")
                                return False

            # after iterating through all possible moves by the black pieces, if none of the moves by the black piece
            # can get black player out of check, change game state accordingly and return True
            self.set_game_state("RED_WON")
            return True

        # if black made the move
        if self.get_turn() == "black":
            # iterate over the red pieces on the board
            for piece in self._red_on_board:
                row_from = piece.get_location()[0]
                column_from = piece.get_location()[1]
                piece_from = self.board()[row_from][column_from]

                # iterate over all squares of the game board
                for row in range(1, 11):
                    for column in range(1, 10):
                        piece_to = self.board()[row][column]

                        # whenever a move is possible to be made by the red piece, make the move if allowed
                        # in order to check if a move can be made by a red piece next turn to not be in check
                        if Piece().checker(self._board, row_from, column_from, row, column) is True:

                            if self.board()[row][column] != '  ':
                                self._black_on_board.remove(self.board()[row][column])
                                self._black_removed.append(self.board()[row][column])
                            self.board()[row][column] = self.board()[row_from][column_from]
                            self.board()[row_from][column_from] = '  '
                            self.board()[row][column].set_location((row, column))

                            # call the check_put_in_check function to check if black still has red in check
                            # if so, reverse the moves and keep iterating
                            if self.check_put_in_check() is True:

                                self.board()[row_from][column_from] = piece_from
                                self.board()[row][column] = piece_to

                                if piece_to != '  ':
                                    self._black_on_board.append(piece_to)
                                    self._black_removed.remove(piece_to)

                                self.board()[row_from][column_from].set_location((row_from, column_from))

                            # call the check_in_check function to check if red piece's move would cause the
                            # flying general situation, and if so, reverse the moves and keep iterating
                            elif self.check_in_check() is False:

                                self.board()[row_from][column_from] = piece_from
                                self.board()[row][column] = piece_to

                                if piece_to != '  ':
                                    self._black_on_board.append(piece_to)
                                    self._black_removed.remove(piece_to)

                                self.board()[row_from][column_from].set_location((row_from, column_from))

                            # if a move by a red piece causes red to not be in check, reverse the moves, set turn,
                            # and return False
                            else:

                                self.board()[row_from][column_from] = piece_from
                                self.board()[row][column] = piece_to

                                if piece_to != '  ':
                                    self._black_on_board.append(piece_to)
                                    self._black_removed.remove(piece_to)

                                self.board()[row_from][column_from].set_location((row_from, column_from))

                                self.set_turn("red")
                                return False

            # after iterating through all possible moves by the red pieces, if none of the moves by the red piece
            # can get red player out of check, change game state accordingly and return True
            self.set_game_state("BLACK_WON")
            return True


class Piece:
    """Represents a Piece with a checker method to check rules concurrent to all of the individual game pieces"""
    def __init__(self):
        """Initializes no data members, a Parent class to subclasses"""
        pass

    def checker(self, board, row_from, column_from, row_to, column_to):
        """
        A checker method to be called by the make move function in the XiangqiGame class to validate moves
        Takes in the board, row/column from and to for making the move as parameters
        """
        # if the row/column given for the piece to be moved is outside of the game board bounds, return False
        if row_from < 1 or row_from > 10:
            return False
        if column_from < 1 or column_from > 9:
            return False

        # if the row/column given for the destination of the piece is outside of the game board bounds, return False
        if row_to < 1 or row_to > 10:
            return False
        if column_to < 1 or column_to > 9:
            return False

        # if the game has already won, return False
        if XiangqiGame().get_game_state() != "UNFINISHED":
            return False

        # if the destination holds a piece that belongs to the player making the move, return False
        if board[row_to][column_to] != '  ':
            if board[row_from][column_from].get_player() == board[row_to][column_to].get_player():
                return False

        # get the type of the piece that is being moved and call its respective is_legal_move function
        # in order to check if the move is valid per specific piece requirements.
        if board[row_from][column_from].get_piece_type().is_legal_move(self, board, row_from, column_from, row_to, column_to) is True:
            return True


class General(Piece):
    """Represents a General game piece with type, location and player"""
    def __init__(self, piece_type, location, player):
        """Returns a General piece with specified parameters"""
        super().__init__()
        self._piece_type = piece_type
        self._location = location
        self._player = player

    def __repr__(self):
        """Sets up repr strings for pieces to be placed on to the game board"""
        if self._player == "black":
            return "bG"
        elif self._player == "red":
            return "rG"

    def get_piece_type(self):
        """Returns the piece's type"""
        return self._piece_type

    def get_location(self):
        """Returns piece's location on the board"""
        return self._location

    def set_location(self, location):
        """Sets the piece's location"""
        self._location = location

    def get_player(self):
        """Returns the player the piece belongs to"""
        return self._player

    def is_legal_move(self, board, row_from, column_from, row_to, column_to):
        """Takes in board, row/column from and to as parameters to check if the made move is legal for the piece"""
        # if the general wants to move diagonally, return False
        if abs(row_from - row_to) == 1 and abs(column_from - column_to) == 1:
            return False

        # if the general moves more than 1 row, return False
        if abs(row_from - row_to) != 0 and abs(row_from - row_to) != 1:
            return False

        # if the general moves more than 1 column, return False
        if abs(column_from - column_to) != 0 and abs(column_from - column_to) != 1:
            return False

        # if the general steps outside of the castle, return False
        if board[row_from][column_from].get_player() == "red":
            if row_to >= 4 or column_to <= 3 or column_to >= 7:
                return False

        if board[row_from][column_from].get_player() == "black":
            if row_to <= 7 or column_to <= 3 or column_to >= 7:
                return False

        # otherwise, return True
        return True


class Adviser(Piece):
    """Represents a Adviser game piece with type, location and player"""
    def __init__(self, piece_type, location, player):
        """Returns a Adviser piece with specified parameters"""
        super().__init__()
        self._piece_type = piece_type
        self._location = location
        self._player = player

    def __repr__(self):
        """Sets up repr strings for pieces to be placed on to the game board"""
        if self._player == "black":
            return "bA"
        if self._player == "red":
            return "rA"

    def get_piece_type(self):
        """Returns the piece's type"""
        return self._piece_type

    def get_location(self):
        """Returns piece's location on the board"""
        return self._location

    def set_location(self, location):
        """Sets the piece's location"""
        self._location = location

    def get_player(self):
        """Returns the player the piece belongs to"""
        return self._player

    def is_legal_move(self, board, row_from, column_from, row_to, column_to):
        """Takes in board, row/column from and to as parameters to check if the made move is legal for the piece"""
        # if the adviser steps outside of the castle, return False
        if board[row_from][column_from].get_player() == "red":
            if row_to >= 4 or column_to <= 3 or column_to >= 7:
                return False

        if board[row_from][column_from].get_player() == "black":
            if row_to <= 7 or column_to <= 3 or column_to >= 7:
                return False

        # if the adviser wants to move orthogonally, return False
        if not (abs(row_from - row_to) == 1 and abs(column_from - column_to) == 1):
            return False

        # otherwise, return True
        return True


class Elephant(Piece):
    """Represents a Elephant game piece with type, location and player"""
    def __init__(self, piece_type, location, player):
        """Returns a Elephant piece with specified parameters"""
        super().__init__()
        self._piece_type = piece_type
        self._location = location
        self._player = player

    def __repr__(self):
        """Sets up repr strings for pieces to be placed on to the game board"""
        if self._player == "black":
            return "bE"
        if self._player == "red":
            return "rE"

    def get_piece_type(self):
        """Returns the piece's type"""
        return self._piece_type

    def get_location(self):
        """Returns piece's location on the board"""
        return self._location

    def set_location(self, location):
        """Sets the piece's location"""
        self._location = location

    def get_player(self):
        """Returns the player the piece belongs to"""
        return self._player

    def is_legal_move(self, board, row_from, column_from, row_to, column_to):
        """Takes in board, row/column from and to as parameters to check if the made move is legal for the piece"""
        # if the elephant piece wants to cross the river, return False
        if board[row_from][column_from].get_player() == 'red':
            if row_to > 5:
                return False

        if board[row_from][column_from].get_player() == 'black':
            if row_to < 6:
                return False

        # Elephant piece is confined to 7 positions while moving two points diagonally without jumping over pieces
        if row_from == 1 and column_from == 3:
            if row_to != 3:
                return False
            if column_to != 1 and column_to != 5:
                return False
            if column_to == 1:
                if board[2][2] != '  ':
                    return False
            if column_to == 5:
                if board[2][4] != '  ':
                    return False

        if row_from == 1 and column_from == 7:
            if row_to != 3:
                return False
            if column_to != 5 and column_to != 9:
                return False
            if column_to == 5:
                if board[2][6] != '  ':
                    return False
            if column_to == 9:
                if board[2][8] != '  ':
                    return False

        if row_from == 3 and column_from == 1:
            if row_to != 1 and row_to != 5:
                return False
            if column_to != 3:
                return False
            if row_to == 1:
                if board[2][2] != '  ':
                    return False
            if row_to == 5:
                if board[4][2] != '  ':
                    return False

        if row_from == 3 and column_from == 5:
            if row_to != 1 and row_to != 5:
                return False
            if column_to != 3 and column_to != 7:
                return False
            if row_to == 1 and column_to == 3:
                if board[2][4] != '  ':
                    return False
            if row_to == 1 and column_to == 7:
                if board[2][6] != '  ':
                    return False
            if row_to == 5 and column_to == 3:
                if board[4][4] != '  ':
                    return False
            if row_to == 5 and column_to == 7:
                if board[4][6] != '  ':
                    return False

        if row_from == 3 and column_from == 9:
            if row_to != 1 and row_to != 5:
                return False
            if column_to != 7:
                return False
            if row_to == 1:
                if board[2][8] != '  ':
                    return False
            if row_to == 5:
                if board[4][8] != '  ':
                    return False

        if row_from == 5 and column_from == 3:
            if row_to != 3:
                return False
            if column_to != 1 and column_to != 5:
                return False
            if column_to == 1:
                if board[4][2] != '  ':
                    return False
            if column_to == 5:
                if board[4][4] != '  ':
                    return False

        if row_from == 5 and column_from == 7:
            if row_to != 3:
                return False
            if column_to != 5 and column_to != 9:
                return False
            if column_to == 5:
                if board[4][6] != '  ':
                    return False
            if column_to == 9:
                if board[4][8] != '  ':
                    return False

        if row_from == 6 and column_from == 3:
            if row_to != 8:
                return False
            if column_to != 1 and column_to != 5:
                return False
            if column_to == 1:
                if board[7][2] != '  ':
                    return False
            if column_to == 5:
                if board[7][4] != '  ':
                    return False

        if row_from == 6 and column_from == 7:
            if row_to != 8:
                return False
            if column_to != 5 and column_to != 9:
                return False
            if column_to == 5:
                if board[7][6] != '  ':
                    return False
            if column_to == 9:
                if board[7][8] != '  ':
                    return False

        if row_from == 8 and column_from == 1:
            if row_to != 6 and row_to != 10:
                return False
            if column_to != 3:
                return False
            if row_to == 6:
                if board[7][2] != '  ':
                    return False
            if row_to == 10:
                if board[9][2] != '  ':
                    return False

        if row_from == 8 and column_from == 5:
            if row_to != 6 and row_to != 10:
                return False
            if column_to != 3 and column_to != 7:
                return False
            if row_to == 6 and column_to == 3:
                if board[7][4] != '  ':
                    return False
            if row_to == 6 and column_to == 7:
                if board[7][6] != '  ':
                    return False
            if row_to == 10 and column_to == 3:
                if board[9][4] != '  ':
                    return False
            if row_to == 10 and column_to == 7:
                if board[9][6] != '  ':
                    return False

        if row_from == 8 and column_from == 9:
            if row_to != 6 and row_to != 10:
                return False
            if column_to != 7:
                return False
            if row_to == 6:
                if board[7][8] != '  ':
                    return False
            if row_to == 10:
                if board[9][8] != '  ':
                    return False

        if row_from == 10 and column_from == 3:
            if row_to != 8:
                return False
            if column_to != 1 and column_to != 5:
                return False
            if column_to == 1:
                if board[9][2] != '  ':
                    return False
            if column_to == 5:
                if board[9][4] != '  ':
                    return False

        if row_from == 10 and column_from == 7:
            if row_to != 8:
                return False
            if column_to != 5 and column_to != 9:
                return False
            if column_to == 5:
                if board[9][6] != '  ':
                    return False
            if column_to == 9:
                if board[9][8] != '  ':
                    return False

        # if a move is allowed, return True
        return True


class Horse(Piece):
    """Represents a Horse game piece with type, location and player"""
    def __init__(self, piece_type, location, player):
        """Returns a Horse piece with specified parameters"""
        super().__init__()
        self._piece_type = piece_type
        self._location = location
        self._player = player

    def __repr__(self):
        """Sets up repr strings for pieces to be placed on to the game board"""
        if self._player == "black":
            return "bH"
        if self._player == "red":
            return "rH"

    def get_piece_type(self):
        """Returns the piece's type"""
        return self._piece_type

    def get_location(self):
        """Returns piece's location on the board"""
        return self._location

    def set_location(self, location):
        """Sets the piece's location"""
        self._location = location

    def get_player(self):
        """Returns the player the piece belongs to"""
        return self._player

    def is_legal_move(self, board, row_from, column_from, row_to, column_to):
        """Takes in board, row/column from and to as parameters to check if the made move is legal for the piece"""
        # if the horse pieces moves beyond two spaces row or column-wise, return False
        if row_to >= row_from + 3:
            return False
        if row_to <= row_from - 3:
            return False
        if column_to >= column_from + 3:
            return False
        if column_to <= column_from - 3:
            return False

        # if the horse piece moves diagonally two spaces, return False
        if row_to == row_from + 2 and column_to == column_from + 2:
            return False
        if row_to == row_from + 2 and column_to == column_from - 2:
            return False
        if row_to == row_from - 2 and column_to == column_from + 2:
            return False
        if row_to == row_from - 2 and column_to == column_from - 2:
            return False

        # if the horse piece moves to upper row, if there is an intervening piece immediately above or the piece moves
        # to the same column, return False
        if row_to == row_from - 2:
            if board[row_from - 1][column_from] != '  ':
                return False
            if column_from == column_to:
                return False

        # if the horse piece moves to lower row, if there is an intervening piece immediately below or the piece moves
        # to the same column, return False
        if row_to == row_from + 2:
            if board[row_from + 1][column_from] != '  ':
                return False
            if column_from == column_to:
                return False

        # if the horse piece moves to lower column, if there is an intervening piece immediately left or the piece moves
        # to the same row, return False
        if column_to == column_from - 2:
            if board[row_from][column_from - 1] != '  ':
                return False
            if row_from == row_to:
                return False

        # if horse piece moves to upper column, if there is an intervening piece immediately right or the piece moves
        # to the same row, return False
        if column_to == column_from + 2:
            if board[row_from][column_from + 1] != '  ':
                return False
            if row_from == row_to:
                return False

        # if the horse piece moves one space diagonally, return False
        if row_to == row_from + 1 and column_to == column_from + 1:
            return False
        if row_to == row_from + 1 and column_to == column_from - 1:
            return False
        if row_to == row_from - 1 and column_to == column_from + 1:
            return False
        if row_to == row_from - 1 and column_to == column_from - 1:
            return False

        # if the horse piece moves one space orthogonally, return False
        if row_to == row_from + 1 and column_to == column_from:
            return False
        if row_to == row_from - 1 and column_to == column_from:
            return False
        if row_to == row_from and column_to == column_from - 1:
            return False
        if row_to == row_from and column_to == column_from + 1:
            return False

        # otherwise, return True
        return True


class Chariot(Piece):
    """Represents a Chariot game piece with type, location and player"""
    def __init__(self, piece_type, location, player):
        """Returns a Chariot piece with specified parameters"""
        super().__init__()
        self._piece_type = piece_type
        self._location = location
        self._player = player

    def __repr__(self):
        """Sets up repr strings for pieces to be placed on to the game board"""
        if self._player == "black":
            return "bC"
        if self._player == "red":
            return "rC"

    def get_piece_type(self):
        """Returns the piece's type"""
        return self._piece_type

    def get_location(self):
        """Returns piece's location on the board"""
        return self._location

    def set_location(self, location):
        """Sets the piece's location"""
        self._location = location

    def get_player(self):
        """Returns the player the piece belongs to"""
        return self._player

    def is_legal_move(self, board, row_from, column_from, row_to, column_to):
        """Takes in board, row/column from and to as parameters to check if the made move is legal for the piece"""
        # if the chariot moves diagonally, return False
        if row_from != row_to and column_from != column_to:
            return False

        # when moving horizontally, if there is an intervening piece between from and to locations, return False
        if row_from == row_to:
            if column_from > column_to:
                x = abs(column_to - column_from)
                for i in range(1, x):
                    if board[row_from][column_from - i] != '  ':
                        return False

            if column_from < column_to:
                x = abs(column_to - column_from)
                for i in range(1, x):
                    if board[row_from][column_from + i] != '  ':
                        return False

        # when moving vertically, if there is an intervening piece between from and to locations, return False
        if column_from == column_to:
            if row_from > row_to:
                x = abs(row_to - row_from)
                for i in range(1, x):
                    if board[row_from - i][column_from] != '  ':
                        return False

            if row_from < row_to:
                x = abs(row_to - row_from)
                for i in range(1, x):
                    if board[row_from + i][column_from] != '  ':
                        return False

        # otherwise, return True
        return True


class Cannon(Piece):
    """Represents a Cannon game piece with type, location and player"""
    def __init__(self, piece_type, location, player):
        """Returns a Cannon piece with specified parameters"""
        super().__init__()
        self._piece_type = piece_type
        self._location = location
        self._player = player

    def __repr__(self):
        """Sets up repr strings for pieces to be placed on to the game board"""
        if self._player == "black":
            return "bN"
        if self._player == "red":
            return "rN"

    def get_piece_type(self):
        """Returns the piece's type"""
        return self._piece_type

    def get_location(self):
        """Returns piece's location on the board"""
        return self._location

    def set_location(self, location):
        """Sets the piece's location"""
        self._location = location

    def get_player(self):
        """Returns the player the piece belongs to"""
        return self._player

    def is_legal_move(self, board, row_from, column_from, row_to, column_to):
        """Takes in board, row/column from and to as parameters to check if the made move is legal for the piece"""

        # if the move is not capturing any opposing piece
        if board[row_to][column_to] == '  ':

            # if the cannon piece is moving diagonally, return False
            if row_from != row_to and column_from != column_to:
                return False

            # when moving horizontally, if there is an intervening piece between from and to locations, return False
            if row_from == row_to:
                if column_from > column_to:
                    x = abs(column_to - column_from)
                    for i in range(1, x):
                        if board[row_from][column_from - i] != '  ':
                            return False

                if column_from < column_to:
                    x = abs(column_to - column_from)
                    for i in range(1, x):
                        if board[row_from][column_from + i] != '  ':
                            return False

            # when moving vertically, if there is an intervening piece between from and to locations, return False
            if column_from == column_to:
                if row_from > row_to:
                    x = abs(row_to - row_from)
                    for i in range(1, x):
                        if board[row_from - i][column_from] != '  ':
                            return False

                if row_from < row_to:
                    x = abs(row_to - row_from)
                    for i in range(1, x):
                        if board[row_from + i][column_from] != '  ':
                            return False

        # if the move is capturing an opposing piece
        else:
            # if the cannon piece is moving diagonally, return False
            if row_from != row_to and column_from != column_to:
                return False

            # when moving horizontally, if the cannon is not jumping over exactly one friend or foe, return False
            friend_or_foe = 0
            if row_from == row_to:
                if column_from > column_to:
                    x = abs(column_to - column_from)
                    for i in range(1, x):
                        if board[row_from][column_from - i] != '  ':
                            friend_or_foe += 1
                    if friend_or_foe != 1:
                        return False

                if column_from < column_to:
                    x = abs(column_to - column_from)
                    for i in range(1, x):
                        if board[row_from][column_from + i] != '  ':
                            friend_or_foe += 1
                    if friend_or_foe != 1:
                        return False

            # moving vertically, if the cannon is not jumping over exactly one friend or foe, return False
            if column_from == column_to:
                if row_from > row_to:
                    x = abs(row_to - row_from)
                    for i in range(1, x):
                        if board[row_from - i][column_from] != '  ':
                            friend_or_foe += 1
                    if friend_or_foe != 1:
                        return False

                if row_from < row_to:
                    x = abs(row_to - row_from)
                    for i in range(1, x):
                        if board[row_from + i][column_from] != '  ':
                            friend_or_foe += 1
                    if friend_or_foe != 1:
                        return False

        # otherwise, return True
        return True


class Solider(Piece):
    """Represents a Soldier game piece with type, location and player"""
    def __init__(self, piece_type, location, player):
        """Returns a Soldier piece with specified parameters"""
        super().__init__()
        self._piece_type = piece_type
        self._location = location
        self._player = player

    def __repr__(self):
        """Sets up repr strings for pieces to be placed on to the game board"""
        if self._player == "black":
            return "bS"
        if self._player == "red":
            return "rS"

    def get_piece_type(self):
        """Returns the piece's type"""
        return self._piece_type

    def get_location(self):
        """Returns piece's location on the board"""
        return self._location

    def set_location(self, location):
        """Sets the piece's location"""
        self._location = location

    def get_player(self):
        """Returns the player the piece belongs to"""
        return self._player

    def is_legal_move(self, board, row_from, column_from, row_to, column_to):
        """Takes in board, row/column from and to as parameters to check if the made move is legal for the piece"""
        # if soldier moves diagonally, return False
        if row_from != row_to and column_from != column_to:
            return False

        # if the piece to be moved belongs to red player
        if board[row_from][column_from].get_player() == 'red':
            # if the piece moves sideways before crossing the river, return False
            if row_from == 4 or row_from == 5:
                if column_from != column_to:
                    return False
                # if the piece does not move exactly one position forward, return False
                if row_to != row_from + 1:
                    return False

            # if the piece already crossed the river
            if row_from >= 6:
                # if the piece does not move rows the piece must move one position sideways, if not, return False
                if row_from == row_to:
                    if column_to != column_from - 1 and column_to != column_from + 1:
                        return False
                # if the piece does not move columns the piece must move one position forward, if not, return False
                if column_from == column_to:
                    if row_to != row_from + 1:
                        return False

        # if the piece to be moved belongs to black player
        if board[row_from][column_from].get_player() == 'black':
            # if the piece moves sideways before crossing the river, return False
            if row_from == 6 or row_from == 7:
                if column_from != column_to:
                    return False
                # if the piece does not move exactly one position forward, return False
                if row_to != row_from - 1:
                    return False

            # if the piece already crossed the river
            if row_from <= 5:
                # if the piece does not move rows the piece must move one position sideways, if not, return False
                if row_from == row_to:
                    if column_to != column_from - 1 and column_to != column_from + 1:
                        return False
                # if the piece does not move columns the piece must move one position forward, if not, return False
                if column_from == column_to:
                    if row_to != row_from - 1:
                        return False
        # otherwise, return True
        return True

