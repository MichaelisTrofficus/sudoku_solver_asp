from sudoku import Sudoku


def generate_board():
    """
    Code to generate the Sudoku board. By default it will be a 9x9 board with 50% of cells empty
    :return: The sudoku board
    """
    return Sudoku(3).difficulty(0.5).board
