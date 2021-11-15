import copy

def playerTurn(board):
    print('Select a column: ')
    column = int(input()) - 1

    res = -1

    if column > board.columns or column < 0:
        print("That's not a valid column")
        return res

    elif board.slots[0][column] != 0:
        print("That column is full")
        return res

    else:
        row = board.rows - 1
        while row >= 0 and res == -1:
            if board.slots[row][column] == 0:
                board.slots[row][column] = 1
                res = 0
            row -= 1

    return res


def __possibleVictories(board, currentPlayer):
    chunk = 4
    res = 0 # Number of possible victories
    column = 0

    while column < board.columns: # For every column of our board
        row = board.rows - 1 # Start at the bottom row
        while row > 0:
            if board.slots[row][column] != currentPlayer:
                i = 0
                while row - i >= 0 and (
                        board.slots[row - i][column] == currentPlayer or board.slots[row - i][column] == 0):
                    i += 1
                    if i == chunk: # If there are 4 in vertical
                        res += 1 # it's a possible victory

                i = 0
                while column + i < board.columns and (
                        board.slots[row][column + i] == currentPlayer or board.slots[row][column + i] == 0):
                    i += 1
                    if i == chunk: # If there are 4 in horizontal
                        res += 1 # it's a possible victory

                i = 0
                while row - i >= 0 and column + i < board.columns and (
                        board.slots[row - i][column + i] == currentPlayer or board.slots[row - i][column + i] == 0):
                    i += 1
                    if i == chunk: # If there are 4 in diagonal right
                        res += 1 # it's a possible victory

                i = 0
                while row - i >= 0 and column - i >= 0 and (
                        board.slots[row - i][column - i] == currentPlayer or board.slots[row - i][column - i] == 0):
                    i += 1
                    if i == chunk: # If there are 4 in diagonal left
                        res += 1 # it's a possible victory

            row -= 1
        column += 1

    return res


def __heuristicCalc(board):
    player_victories = __possibleVictories(board, currentPlayer=1)
    computer_victories = __possibleVictories(board, currentPlayer=2)

    return computer_victories - player_victories


def __moveGenerator(board, turn, depth=2):
    best_heuristic = int()  # Best heuristic value
    column = 0  # Current column
    while column < board.columns:  # While there are unvisited columns
        done = -1  # We only want to check the move that gravity allows
        row = board.rows - 1  # Start at the bottom of the column
        while row >= 0 and done == -1 and turn <= depth:  # there are slots in the column and we haven't reached depth
            if board.slots[row][column] == 0:  # If they are empty
                board.slots[row][column] = 2  # We make the move
                heuristic = __moveGenerator(board=board, turn=turn + 1,
                                            depth=depth)  # We analyse the best outcome out of the move we made
                heuristic += __heuristicCalc(board)  # in consecutive moves assuming minimax frame
                if turn % 2 == 0:
                    if heuristic > best_heuristic:  # If we find a better outcome than our best yet
                        best_heuristic = heuristic  # we assign it as our solution

                else:
                    if heuristic < best_heuristic:  # If we find a better outcome than their best yet
                        best_heuristic = heuristic  # we assign it as our solution

                board.slots[row][column] = 0  # We undo the move to continue analysis
                done = 0  # We check the gravity marker so we don't break physics
            row -= 1  # We move up a row
        column += 1  # We move up a column

    return best_heuristic  # We propagate the final heuristic


def miniMaxMove(board, depth=2):
    print('Computer Turn: ')
    best_heuristic = int()  # Best heuristic value
    turn = 0
    best_state = copy.deepcopy(board)  # Best move according to analysis
    column = 0  # Current column
    while column < board.columns:  # While there are unvisited columns
        done = -1  # We only want to check the move that gravity allows
        row = board.rows - 1  # Start at the bottom of the column
        while row >= 0 and done == -1 and turn < depth:  # there are slots in the column and we haven't reached depth
            if board.slots[row][column] == 0:  # If they are empty
                board.slots[row][column] = 2  # We make the move
                heuristic = __moveGenerator(board=board, turn=turn + 1,
                                depth=depth)  # We analyse the best outcome out of the move we made
                heuristic += __heuristicCalc(board)  # in consecutive moves assuming minimax frame
                if heuristic >= best_heuristic:  # If we find a better outcome than our best yet
                    best_heuristic = heuristic  # we assign it as our solution
                    best_state = copy.deepcopy(board)  # copy the board to an aux var so we don't alter it
                board.slots[row][column] = 0  # We undo the move to continue analysis
                done = 0  # We check the gravity marker so we don't break physics
            row -= 1  # We move up a row
        column += 1  # We move up a column

    return best_state  # We set the board as our best case scenario


def victoryCheck(board, currentPlayer): # Practically identical to possibleVictories function
    chunk = 4
    res = 3
    column = 0

    i = 0
    while i < board.columns and res == 3: # We check for a tie by seeing if there are empty slots left
        if board.slots[0][i] == 0:
            res = 0
        i += 1

    while column < board.columns and res == 0: # For every column
        row = board.rows - 1
        while row > 0 and res == 0: # We check every row
            i = 0
            while row - i >= 0 and board.slots[row - i][column] == currentPlayer: # That has a currentPlayer piece
                i += 1
                if i == chunk: # If there are 4 in vertical
                    res = currentPlayer # currentPlayer won

            i = 0
            while column + i < board.columns and board.slots[row][column + i] == currentPlayer:
                i += 1
                if i == chunk: # If there are 4 in  horizontal
                    res = currentPlayer # currentPlayer won

            i = 0
            while row - i >= 0 and column + i < board.columns and board.slots[row - i][column + i] == currentPlayer:
                i += 1
                if i == chunk: # If there are 4 in diagonal right
                    res = currentPlayer # currentPlayer won

            i = 0
            while row - i >= 0 and column - i >= 0 and board.slots[row - i][column - i] == currentPlayer:
                i += 1
                if i == chunk: # If there are 4 in diagonal left
                    res = currentPlayer # currentPlayer won
            row -= 1
        column += 1

    return res # We return the winning player, or tie, or keep playin { 1 or 2, 3, 0}
