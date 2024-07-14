# # Создаем игровое поле
# board = [' ' for _ in range(9)]

# def print_board():
#     for i in range(0, 9, 3):
#         print(board[i], '|', board[i+1], '|', board[i+2])

# def make_move(player, position):
#     board[position] = player

# def is_winner(player):
#     if (board[0] == board[1] == board[2] == player or
#         board[3] == board[4] == board[5] == player or
#         board[6] == board[7] == board[8] == player or
#         board[0] == board[3] == board[6] == player or
#         board[1] == board[4] == board[7] == player or
#         board[2] == board[5] == board[8] == player or
#         board[0] == board[4] == board[8] == player or
#         board[2] == board[4] == board[6] == player):
#         return True
#     return False

# def is_board_full():
#     if ' ' in board:
#         return False
#     return True

# # Цикл игры
# while True:
#     print_board()
    
#     # Ход игрока 1 (крестики)
#     move = int(input("Игрок 1 (X), выберите позицию для хода: "))
#     make_move('X', move)
#     if is_winner('X'):
#         print_board()
#         print("Игрок 1 победил!")
#         break
#     if is_board_full():
#         print_board()
#         print("Ничья!")
#         break
    
#     # Ход игрока 2 (нолики)
#     move = int(input("Игрок 2 (O), выберите позицию для хода: "))
#     make_move('O', move)
#     if is_winner('O'):
#         print_board()
#         print("Игрок 2 победил!")
#         break
#     if is_board_full():
#         print_board()
#         print("Ничья!")
#         break

# Создаем игровое поле
board = [str(i+1) for i in range(9)]

def print_board():
    for i in range(0, 9, 3):
        print(board[i], '|', board[i+1], '|', board[i+2])

def make_move(player, position):
    board[position-1] = player

def is_winner(player):
    if (board[0] == board[1] == board[2] == player or
        board[3] == board[4] == board[5] == player or
        board[6] == board[7] == board[8] == player or
        board[0] == board[3] == board[6] == player or
        board[1] == board[4] == board[7] == player or
        board[2] == board[5] == board[8] == player or
        board[0] == board[4] == board[8] == player or
        board[2] == board[4] == board[6] == player):
        return True
    return False

def is_board_full():
    if 'X' in board or 'O' in board:
        return False
    return True

# Цикл игры
while True:
    print_board()
    
    # Ход игрока 1 (крестики)
    move = int(input("Игрок 1 (X), выберите позицию для хода: "))
    make_move('X', move)
    if is_winner('X'):
        print_board()
        print("Игрок 1 победил!")
        break
    if is_board_full():
        print_board()
        print("Ничья!")
        break
    
    # Ход игрока 2 (нолики)
    move = int(input("Игрок 2 (O), выберите позицию для хода: "))
    make_move('O', move)
    if is_winner('O'):
        print_board()
        print("Игрок 2 победил!")
        break
    if is_board_full():
        print_board()
        print("Ничья!")
        break