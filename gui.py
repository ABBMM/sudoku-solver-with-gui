import pygame
import solver

# STARTER GRID
grid = [[7, 8, 0, 4, 0, 0, 1, 2, 0],
        [6, 0, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 0, 6, 0, 1, 0, 7, 8],
        [0, 0, 7, 0, 4, 0, 2, 6, 0],
        [0, 0, 1, 0, 5, 0, 9, 3, 0],
        [9, 0, 4, 0, 6, 0, 0, 0, 5],
        [0, 7, 0, 3, 0, 0, 0, 1, 2],
        [1, 2, 0, 0, 0, 7, 4, 0, 0],
        [0, 4, 9, 2, 0, 6, 0, 0, 7]]

pygame.init()

# WINDOW SETTINGS
WIDTH, HEIGHT = 600, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sudoku Solver")

# VARIABLES
WHITE: tuple[int, int, int] = (255, 255, 255)
BLACK: tuple[int, int, int] = (0, 0, 0)
RED: tuple[int, int, int] = (255, 0, 0)
LIGHT_BLUE: tuple[int, int, int] = (173, 216, 230)
YELLOW: tuple[int, int, int] = (255, 255, 0)
FPS: int = 60
SPACE: float = WIDTH / 9
NUMBER_FONT = pygame.font.SysFont("Crash Chassis", 60)
GRID_X: int = 0
GRID_Y: int = 0
NUMBER: int = 1


# UPDATES WINDOW
def draw_window():
    WIN.fill(BLACK)
    grid_draw(GRID_X, GRID_Y)
    grid_initial()
    pygame.display.update()


# DRAWS STARTER GRID
def grid_initial():
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j] != 0:
                number_text = NUMBER_FONT.render(str(grid[i][j]), True, WHITE)
                WIN.blit(number_text, ((i * SPACE + SPACE // 3) // 2 * 2, (j * SPACE + SPACE // 4) // 2 * 2))


# CHECKS IF NUMBER PLACED IS VALID
def valid(n, x, y):
    if solver.check(n, x, y, grid):
        grid[x][y] = n


# DRAWS NUMBERS AND OUTLINE BOX
def grid_draw(x, y):
    for i in range(10):
        if i % 3 == 0:
            thickness = 7
        else:
            thickness = 2
        pygame.draw.line(WIN, WHITE, (i * SPACE, 0), (i * SPACE, WIDTH), thickness)
        pygame.draw.line(WIN, WHITE, (0, i * SPACE), (HEIGHT, i * SPACE), thickness)
    box = pygame.Rect(x * SPACE + 1, y * SPACE + 1, SPACE, SPACE)
    pygame.draw.rect(WIN, LIGHT_BLUE, box, 10)


# MAIN FUNCTION (60FPS)
def main():
    run = True
    global GRID_X, GRID_Y, NUMBER, grid
    clock = pygame.time.Clock()
    while run:
        clock.tick(FPS)
        # EXIT CONDITIONS
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                break
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
                    pygame.quit()
                    break
            # GRID MOVEMENT
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if GRID_X == 0:
                        GRID_X = 8
                    else:
                        GRID_X -= 1
                if event.key == pygame.K_RIGHT:
                    if GRID_X == 8:
                        GRID_X = 0
                    else:
                        GRID_X += 1
                if event.key == pygame.K_UP:
                    if GRID_Y == 0:
                        GRID_Y = 8
                    else:
                        GRID_Y -= 1
                if event.key == pygame.K_DOWN:
                    if GRID_Y == 8:
                        GRID_Y = 0
                    else:
                        GRID_Y += 1
                # NUMBER INPUT
                if event.key == pygame.K_1:
                    valid(1, GRID_X, GRID_Y)
                if event.key == pygame.K_2:
                    valid(2, GRID_X, GRID_Y)
                if event.key == pygame.K_3:
                    valid(3, GRID_X, GRID_Y)
                if event.key == pygame.K_4:
                    valid(4, GRID_X, GRID_Y)
                if event.key == pygame.K_5:
                    valid(5, GRID_X, GRID_Y)
                if event.key == pygame.K_6:
                    valid(6, GRID_X, GRID_Y)
                if event.key == pygame.K_7:
                    valid(7, GRID_X, GRID_Y)
                if event.key == pygame.K_8:
                    valid(8, GRID_X, GRID_Y)
                if event.key == pygame.K_9:
                    valid(9, GRID_X, GRID_Y)
                if event.key == pygame.K_BACKSPACE:
                    grid[GRID_X][GRID_Y] = 0

                # SOLVES PUZZLE
                if event.key == pygame.K_RETURN:
                    solver.solve(grid)
            draw_window()


if __name__ == "__main__":
    main()
