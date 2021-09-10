import sys
import pygame

from asp_sudoku_solver.buttons import Button
from asp_sudoku_solver.generator import generate_board
from asp_sudoku_solver.asp_solver import solve
from asp_sudoku_solver.helpers.transformations import convert_to_clingo, fill_gaps

pygame.init()

# CONSTANTS
WINDOW_WIDTH = 450
WINDOW_HEIGHT = 510
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLOCK_SIZE = 50

# SCREEN / WINDOW OBJECT DEFINITION
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Sudoku Solver with ASP')

# CLOCK
clock = pygame.time.Clock()

# FONT
gui_font = pygame.font.Font(None, 30)


button = Button(screen, gui_font, "Solve", 70, 30, (200, 470))


def draw_grid(b):
    for i in range(0, WINDOW_WIDTH, BLOCK_SIZE):
        for j in range(0, 450, BLOCK_SIZE):
            rect = pygame.Rect(i, j, BLOCK_SIZE, BLOCK_SIZE)
            pygame.draw.rect(screen, BLACK, rect, 1)

            i_sudoku = i // 50
            j_sudoku = j // 50

            if (i_sudoku % 3) == 0:
                pygame.draw.line(screen, (0, 0, 0), (i_sudoku*50, 0), (i_sudoku*50, 450), 6)

            if (j_sudoku % 3) == 0:
                pygame.draw.line(screen, (0, 0, 0), (0, j_sudoku * 50), (450, j_sudoku * 50), 6)

            sudoku_number = b[i_sudoku][j_sudoku]
            if sudoku_number:
                text_number = gui_font.render(str(sudoku_number), 1, (0, 0, 0))
                screen.blit(text_number, (i + 25, j + 25))


def init_board():

    # GENERATE AN INITIAL SUDOKU BOARD
    board = generate_board()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill((255, 255, 255))
        draw_grid(board)

        if button.draw():
            board_clingo = convert_to_clingo(board)
            clingo_sol = solve(board_clingo)

            board = fill_gaps(board, clingo_sol)

        pygame.display.update()
        clock.tick(60)
