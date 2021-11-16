import BoardClass
import GameFunc

def game(board):
    victory = 0
    turn = 0
    while victory == 0:

        if turn % 2 == 0:
            validity = -1
            while validity == -1:
                validity = GameFunc.playerTurn(board)

            victory = GameFunc.victoryCheck(board=board, currentPlayer=1)

        else:
            board = GameFunc.miniMaxMove(board, depth=4)
            victory = GameFunc.victoryCheck(board=board, currentPlayer=2)

        turn += 1
        board.__print__()

    if victory == 1:
        print('You win!')
        print('Congrats!')

    elif victory == 2:
        print('You lose')
        print('Better luck next time!')

    elif victory == 3:
        print("It's a tie!")

    return


# We initialize our board
startBoard = BoardClass.BoardClass(rows=6, columns=6)
depth = 3
startBoard.__print__()

game(startBoard)
