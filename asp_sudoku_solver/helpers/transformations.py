
def convert_to_clingo(array):
    output = ""

    for i in range(9):
        for j in range(9):
            if array[i][j]:
                output += f" state({i+1}, {j+1}, {array[i][j]}). "
    return output


def fill_gaps(initial_board, clingo_sol):

    clingo_sol_ref = []
    for i in clingo_sol:
        clingo_sol_ref.append([int(i[6]) - 1, int(i[8]) - 1, int(i[10])])

    for i in clingo_sol_ref:
        initial_board[i[0]][i[1]] = i[2]

    return initial_board
