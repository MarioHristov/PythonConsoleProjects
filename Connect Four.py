# Exceptions
class InvalidColumnError(Exception):
    pass


class FullColumnError(Exception):
    pass


class ConnectFour:
    def __init__(self, rows=6, columns=7):
        self.rows = rows
        self.columns = columns
        self.matrix = [[0 for i in range(7)] for m in range(6)]

    # №8 Check if there are connecting four column/row/diagonals
    def check_row(self, player_turn, *args, count=0):
        for elem in self.matrix[args[0]]:
            if elem != player_turn:
                count = 0
            else:
                count += 1
            if count == 4:
                break
        return count

    def check_col(self, player_turn, *args, count=0):
        for i in range(self.rows):
            if self.matrix[i][args[0]] != player_turn:
                count = 0
            else:
                count += 1
            if count == 4:
                break
        return count

    def check_left_to_right_diagonal(self, player_turn, *args, count=0):
        row = args[0]
        col = args[1]
        while 0 < row and 0 < col:
            row -= 1
            col -= 1

        while (row < self.rows and col < self.columns) and count < 4:
            if self.matrix[row][col] != player_turn:
                count = 0
            else:
                count += 1

            row += 1
            col += 1


    def check_right_to_left_diagonal(self, player_turn, *args, count=0):
        row = args[0]
        col = args[1]
        while 0 < row and col < self.columns - 1:
            row -= 1
            col += 1

        while (row < self.rows and 0 <= col) and count < 4:
            if self.matrix[row][col] != player_turn:
                count = 0
            else:
                count += 1

            row += 1
            col -= 1

    # №7 Check if there is a winner
    def is_winner(self, player_turn, number_location_on_board):
        slot_count = 4

        row = number_location_on_board[0]
        col = number_location_on_board[1]

        check_col = (self.check_row(player_turn, row) == slot_count)
        check_row = (self.check_col(player_turn, col) == slot_count)
        check_diagonal_right_left = (
                self.check_right_to_left_diagonal(player_turn, row, col) == slot_count)
        check_diagonal_left_right = (
                self.check_left_to_right_diagonal(player_turn, row, col) == slot_count)

        result = any(
            elem is True for elem in [check_col, check_row, check_diagonal_right_left, check_diagonal_left_right])
        return result

    # №6 Place the number at the correct spot
    def place_player_choice(self, _column, player):
        for row in range(len(self.matrix) - 1, -1, -1):
            if self.matrix[row][_column] == 0:
                self.matrix[row][_column] = player
                return [row, _column]
        raise FullColumnError

    # №4 Validate player input
    def validate_input(self, column):
        if not (0 < column <= self.columns):
            raise InvalidColumnError

    # №2 Print the matrix
    def print_matrix(self):
        for i in range(len(self.matrix)):
            print(self.matrix[i])

    def is_draw(self):
        if 0 not in self.matrix[0]:
            return True
        else:
            return False


def start_game():
    game = ConnectFour()
    # №1 Create a matrix
    game.print_matrix()

    player_in_turn = 1

    while True:
        # №5 Have player turns
        player_in_turn = 2 if player_in_turn % 2 == 0 else 1
        try:
            # №3 Have a player input
            column_to_place = int(input(f"Player {player_in_turn}, please choose a column:\n "))

            game.validate_input(column_to_place)

            position_on_board = game.place_player_choice(column_to_place - 1, player_in_turn)

            game.print_matrix()

            if game.is_winner(player_in_turn, position_on_board):
                print(f"Player {player_in_turn} won!")
                break
            elif game.is_draw():
                print(f"No more places to fill, seems like a draw to me?!")
                break

        except InvalidColumnError:
            print("Please input valid column! Between 1-7")
            continue

        except ValueError:
            print("Input a digit!")
            continue

        except FullColumnError:
            print("Column is full choose another one!")
            continue

        player_in_turn += 1


if __name__ == '__main__':
    start_game()
