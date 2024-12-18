import pygame
import random
import sys

pygame.init()

WIDTH, HEIGHT = 1100, 900
TILE_SIZE = 40

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)
CYAN = (0, 255, 255)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pacman")

font = pygame.font.SysFont(None, 36)

LEVEL = [
    "############################",
    "#............##............#",
    "#.####.#####.##.#####.####.#",
    "#.#  #.#   #.##.#   #.#  #.#",
    "#.####.#####.##.#####.####.#",
    "#..........................#",
    "#.####.##.########.##.####.#",
    "#.####.##.########.##.####.#",
    "#......##....##....##......#",
    "######.##### ## #####.######",
    "     #.##### ## #####.#     ",
    "######.##          ##.######",
    "       .## ######## ##.     ",
    "######.## ######## ##.######",
    "     #.##          ##.#     ",
    "######.##### ## #####.######",
    "#............##............#",
    "#.####.#####.##.#####.####.#",
    "#.#  #.#   #.##.#   #.#  #.#",
    "#.####.#####.##.#####.####.#",
    "#..........................#",
    "############################",
]

class Pacman:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.dx = 0
        self.dy = 0
        self.speed = 2

    def update(self):
        new_x = self.x + self.dx * self.speed
        new_y = self.y + self.dy * self.speed

        if not is_wall(new_x, self.y):
            self.x = new_x
        if not is_wall(self.x, new_y):
            self.y = new_y

        row = self.y // TILE_SIZE
        col = self.x // TILE_SIZE
        if LEVEL[row][col] == ".":
            global score
            score += 10
            LEVEL[row] = LEVEL[row][:col] + " " + LEVEL[row][col+1:]

    def draw(self):
        pygame.draw.circle(screen, YELLOW, (self.x, self.y), TILE_SIZE // 2 - 2)

class Ghost:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.direction = random.choice([(1, 0), (-1, 0), (0, 1), (0, -1)])
        self.speed = 2

    def update(self):
        new_x = self.x + self.direction[0] * self.speed
        new_y = self.y + self.direction[1] * self.speed

        if is_wall(new_x, new_y):
            self.direction = random.choice([(1, 0), (-1, 0), (0, 1), (0, -1)])
        else:
            self.x = new_x
            self.y = new_y

    def draw(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), TILE_SIZE // 2 - 2)

def is_wall(x, y):
    row = y // TILE_SIZE
    col = x // TILE_SIZE
    if row < 0 or col < 0 or row >= len(LEVEL) or col >= len(LEVEL[0]):
        return True
    return LEVEL[row][col] == "#"

def check_game_end():
    for row in LEVEL:
        if "." in row:
            return False
    return True

player = Pacman(60, 60)
ghosts = [
    Ghost(200, 200, RED),
    Ghost(600, 400, BLUE),
    Ghost(120, 60, GREEN),
    Ghost(900, 60, PURPLE),
    Ghost(400, 600, ORANGE),
    Ghost(500, 700, CYAN)
]

score = 0

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player.dx, player.dy = 0, -1
            elif event.key == pygame.K_DOWN:
                player.dx, player.dy = 0, 1
            elif event.key == pygame.K_LEFT:
                player.dx, player.dy = -1, 0
            elif event.key == pygame.K_RIGHT:
                player.dx, player.dy = 1, 0

    player.update()
    for ghost in ghosts:
        ghost.update()

    for ghost in ghosts:
        if abs(player.x - ghost.x) < TILE_SIZE // 2 and abs(player.y - ghost.y) < TILE_SIZE // 2:
            screen.fill(BLACK)
            game_over_text = font.render("Game Over!", True, RED)
            screen.blit(game_over_text, (WIDTH // 2 - 100, HEIGHT // 2))
            pygame.display.flip()
            pygame.time.wait(3000)
            pygame.quit()
            sys.exit()

    if check_game_end():
        screen.fill(BLACK)
        win_text = font.render("You Win!", True, YELLOW)
        screen.blit(win_text, (WIDTH // 2 - 100, HEIGHT // 2))
        pygame.display.flip()
        pygame.time.wait(3000)
        pygame.quit()
        sys.exit()

    screen.fill(BLACK)

    for row in range(len(LEVEL)):
        for col in range(len(LEVEL[row])):
            if LEVEL[row][col] == "#":
                pygame.draw.rect(screen, BLUE, (col * TILE_SIZE, row * TILE_SIZE, TILE_SIZE, TILE_SIZE))
            elif LEVEL[row][col] == ".":
                pygame.draw.circle(screen, WHITE, (col * TILE_SIZE + TILE_SIZE // 2, row * TILE_SIZE + TILE_SIZE // 2), 4)

    player.draw()
    for ghost in ghosts:
        ghost.draw()

    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(30)
