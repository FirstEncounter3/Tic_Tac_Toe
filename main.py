import sys
from random import randint
from time import sleep


SYMBOL_LIST = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
INDEX_LIST = []

def intro(t) -> None:
    print(' _    _    _____      ______                   ')
    sleep(t)
    print('\ \  / /  / ___ \    / _____)                  ')
    sleep(t)
    print(' \ \/ /__| |   | |  | /  ___  ____ ____   ____ ')
    sleep(t)
    print('  )  (___) |   | |  | | (___)/ _  |    \ / _  )')
    sleep(t)
    print(' / /\ \  | |___| |  | \____/( ( | | | | ( (/ / ')
    sleep(t)
    print('/_/  \_\  \_____/    \_____/ \_||_|_|_|_|\____)')
    sleep(t)
    print('                                               ')
    sleep(t)


def choose_mods() -> int:
    while True:
        try:
            coop = int(input('Выберите режим игры: 1 - для игры с другом, 2 - для игры с компьютером > '))
            if coop == 1:
                print('Выбран режим игры с другом\n')
                return coop
            if coop == 2:
                print('Выбран режим игры с компьютером\n')
                return coop
            print('Режим не выбран или есть ошибки ввода. Попробуйте еще раз')
        except ValueError:
            print('Ошибка ввода: введено не число')


def choose_players(symbol: str) -> str:
    return input(f'Введите имя игрока, который будет играть за {symbol}: ')

def win_or_not(symbol_list: list, player_one, player_two) -> str:

    top_horizontal = [symbol_list[0], symbol_list[1], symbol_list[2]]
    middle_horizontal = [symbol_list[3],symbol_list[4],symbol_list[5]]
    bottom_horizontal = [symbol_list[6], symbol_list[7], symbol_list[8]]

    left_vertical = [symbol_list[0], symbol_list[3], symbol_list[6]]
    middle_vertical = [symbol_list[1], symbol_list[4], symbol_list[7]]
    right_vertical = [symbol_list[2], symbol_list[5], symbol_list[8]]

    left_diagonal = [symbol_list[0], symbol_list[4], symbol_list[8]]
    right_diagonal = [symbol_list[2], symbol_list[4], symbol_list[6]]

    if (
            all(i == "X" for i in top_horizontal)
            or all(i == "X" for i in middle_horizontal)
            or all(i == "X" for i in bottom_horizontal)
            or all(i == "X" for i in left_vertical)
            or all(i == "X" for i in middle_vertical)
            or all(i == "X" for i in right_vertical)
            or all(i == "X" for i in left_diagonal)
            or all(i == "X" for i in right_diagonal)
    ):
        print(f"Выиграл {player_one}! Поздравляем!")
        sys.exit()

    if (
            all(i == "O" for i in top_horizontal)
            or all(i == "O" for i in middle_horizontal)
            or all(i == "O" for i in bottom_horizontal)
            or all(i == "O" for i in left_vertical)
            or all(i == "O" for i in middle_vertical)
            or all(i == "O" for i in right_vertical)
            or all(i == "O" for i in left_diagonal)
            or all(i == "O" for i in right_diagonal)
    ):
        print(f"Выиграл {player_two}! Поздравляем!")
        sys.exit()
    else:
        return '...'


def player_input(player: str) -> int:
    while True:
        try:
            symbol_index = int(input(f'Игрок {player} выберите свободную ячейку от 1-9 > '))
            symbol_index -= 1

            if 0 <= symbol_index < 10:
                if symbol_index in INDEX_LIST:
                    print('Ячейка занята!')
                    continue
                INDEX_LIST.append(symbol_index)
                return symbol_index
            print('Выбрана ячейка за пределами 1-9. Попробуйте снова')
        except ValueError:
            print('Ошибка ввода: введено не число')


def comp_input() -> int:
    while True:
        symbol_index = randint(0, 9)
        symbol_index -= 1

        if symbol_index in INDEX_LIST:
            continue

        INDEX_LIST.append(symbol_index)

        return symbol_index


def create_board(symbol: list) -> None:
    print('\n' + '*' * 11)
    print(f" {symbol[0]} | {symbol[1]} | {symbol[2]}")
    print("---|---|---")
    print(f" {symbol[3]} | {symbol[4]} | {symbol[5]}")
    print("---|---|---")
    print(f" {symbol[6]} | {symbol[7]} | {symbol[8]}")
    print('*' * 11 + '\n')


def game():
    intro(0.2)
    print('Игра "Крестики-Нолики". Два игрока поочередно выбирают ячейку, в соответствии с их символом X или O.\n')

    mod = choose_mods()

    if mod == 1:
        player_one = choose_players('X')
        player_two = choose_players('O')

        print(f'Игрок {player_one} (X) играет против {player_two} (O)')
        create_board(SYMBOL_LIST)

        for i in range(0, 9):
            if i % 2 == 0:
                index = player_input(player_one)
                SYMBOL_LIST[index] = 'X'
            else:
                index = player_input(player_two)
                SYMBOL_LIST[index] = 'O'
            create_board(SYMBOL_LIST)
            win_or_not(SYMBOL_LIST, player_one, player_two)

    if mod == 2:
        player_one = choose_players('X')
        player_two = 'Computer'
        print(f'Игрок {player_one} (X) играет против компьютера (O)')

        create_board(SYMBOL_LIST)

        for i in range(0, 9):
            if i % 2 == 0:
                index = player_input(player_one)
                SYMBOL_LIST[index] = 'X'
            else:
                print("Ход компьютера...")
                index = comp_input()
                print(f"Компьютер выбрал ячейку {index+1}")
                SYMBOL_LIST[index] = 'O'
            create_board(SYMBOL_LIST)
            win_or_not(SYMBOL_LIST, player_one, player_two)


if __name__ == "__main__":
    game()
