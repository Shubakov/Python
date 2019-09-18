def get_cells(chess_piece: str, cell: str):
    chess_piece = chess_piece.lower()
    letter_coordinate = cell[0].upper()
    number_coordinate = int(cell[1])
    result = []
    if number_coordinate > 8 or number_coordinate < 1 or letter_coordinate < "A" or letter_coordinate > "H":
        return
    if chess_piece == "пешка":
        if number_coordinate == 8:
            return []
        return letter_coordinate + str(number_coordinate + 1) if number_coordinate != 2 else [
            letter_coordinate + str(number_coordinate + 1), letter_coordinate + str(number_coordinate + 2)]
    elif chess_piece == "король":
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue
                get_result(i, j, letter_coordinate, number_coordinate, result)
        return result
    elif chess_piece == "ферзь" or chess_piece == "слон" or chess_piece == "ладья":
        for i in range(-8, 8):
            for j in range(-8, 8):
                if i == 0 and j == 0:
                    continue
                if chess_piece == "ферзь" and (i == 0 or j == 0 or i == j):
                    get_result(i, j, letter_coordinate, number_coordinate, result)
                elif chess_piece == "слон" and (i == j):
                    get_result(i, j, letter_coordinate, number_coordinate, result)
                elif chess_piece == "ладья" and (i == 0 or j == 0):
                    get_result(i, j, letter_coordinate, number_coordinate, result)
        return result
    elif chess_piece == "конь":
        delta = [-2, -1, 1, 2]
        for i in delta:
            for j in delta:
                if abs(i) != abs(j):
                    get_result(i, j, letter_coordinate, number_coordinate, result)
        return result


def get_result(i, j, letter_coordinate, number_coordinate, result):
    if "A" <= chr(ord(letter_coordinate) + i) <= "H" and 1 <= number_coordinate + j <= 8:
        result.append(chr(ord(letter_coordinate) + i) + str(number_coordinate + j))


print(get_cells("Пешка", "A1"))
print(get_cells("король", "b7"))
print(get_cells("ферзь", "a2"))
print(get_cells("ладья", "a2"))
print(get_cells("слон", "a2"))
print(get_cells("конь", "f5"))
