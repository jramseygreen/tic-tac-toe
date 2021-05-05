import random


def show_board(board):
    print("")
    print("|".join(board[0]))
    print("-----")
    print("|".join(board[1]))
    print("-----")
    print("|".join(board[2]))


def get_player_move(board):
    try:
        return int(input("Enter the coordinates of your next move (XY): "))
    except:
        print("please enter a valid move!")
        show_board(board)
        return get_player_move(board)


def do_cpu_move(board):
    while not check_move(board, random.randint(0, 2) * 10 + random.randint(0, 2), False):
        pass


def check_move(board, move, turn):
    global WINNER
    y = move // 10
    x = move % 10
    won = False

    try:
        if board[x][y] == " ":
            make_move(board, move, turn)

            # x dir
            won = "".join(board[x]).replace(board[x][y], "") == ""

            if not won:
                # y dir
                for i in range(len(board[0])):
                    if board[x][y] == board[i][y]:
                        won = True
                    else:
                        won = False
                        break

            if not won:
                # diagonal
                if (x + y) % 2 == 0:
                    for i in range(len(board[0])):
                        if board[x][y] == board[i][i]:
                            won = True
                        else:
                            won = False
                            break

                    if not won:
                        for i in range(len(board[0])):
                            if board[x][y] == board[len(board[0]) - (i+1)][i]:
                                won = True
                            else:
                                won = False
                                break

            if won:
                if turn:
                    WINNER = "Player 1"
                else:
                    WINNER = "Player 2"

            return True
    except:
        pass
    return False


def make_move(board, move, turn):
    if turn:
        board[move % 10][move // 10] = "x"
    else:
        board[move % 10][move // 10] = "o"


WINNER = ""
if __name__ == "__main__":
    board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    turn = True
    opponent = input("Play against human or computer? ").lower()

    while WINNER == "":
        show_board(board)
        move = ""
        if turn:
            print("\nPlayer 1's turn.")
        else:
            print("\nPlayer 2's turn.")

        if opponent == "human" or turn:
            move = get_player_move(board)
            if check_move(board, move, turn):
                turn = not turn
            else:
                print("please enter a valid move!")
        else:
            if not turn:
                do_cpu_move(board)
                turn = not turn

    show_board(board)
    print("The winner is", WINNER, "!")
