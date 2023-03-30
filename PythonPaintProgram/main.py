import os,openai,random,requests,shutil,pyautogui
from utils import * 
from skimage import io
from artif import generatePrompt, generateImage
from threading import Thread
import matplotlib
from screenshotting import saveImage

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Slow Draw")


prompt = generatePrompt()



font = pygame.font.Font('freesansbold.ttf', 15)
text = font.render(prompt, True, (0, 0, 0), (255, 255, 255))
textRect = text.get_rect()
textRect.center = (WIDTH/2, textRect.height)

def init_grid(rows, cols, color):
    grid = []

    for i in range(rows):
        grid.append([])
        for _ in range(cols):
            grid[i].append(color)

    return grid


def draw_grid(win, grid):
    for i, row in enumerate(grid):
        for j, pixel in enumerate(row):
            pygame.draw.rect(win, pixel, (j * PIXEL_SIZE, i *
                                          PIXEL_SIZE, PIXEL_SIZE, PIXEL_SIZE))

    if DRAW_GRID_LINES:
        for i in range(ROWS + 1):
            pygame.draw.line(win, BLACK, (0, i * PIXEL_SIZE),
                             (WIDTH, i * PIXEL_SIZE))

        for i in range(COLS + 1):
            pygame.draw.line(win, BLACK, (i * PIXEL_SIZE, 0),
                             (i * PIXEL_SIZE, HEIGHT - TOOLBAR_HEIGHT))


def draw(win, grid, buttons):
    win.fill(BG_COLOR)
    draw_grid(win, grid)
    win.blit(text, textRect)


    for button in buttons:
        button.draw(win)

    pygame.display.update()


def get_row_col_from_pos(pos):
    x, y = pos
    row = y // PIXEL_SIZE
    col = x // PIXEL_SIZE

    if row >= ROWS:
        raise IndexError

    return row, col


run = True
clock = pygame.time.Clock()
grid = init_grid(ROWS, COLS, BG_COLOR)
drawing_color = BLACK

button_y = HEIGHT - TOOLBAR_HEIGHT/2 - 25
buttons = [
    Button(10, button_y, 50, 50, BLACK),
    Button(70, button_y, 50, 50, RED),
    Button(130, button_y, 50, 50, GREEN),
    Button(190, button_y, 50, 50, BLUE),
    Button(250,button_y,50,50,ORANGE),
    Button(250,button_y,50,50,YELLOW),
    Button(310,button_y,50,50,ORANGE),
    Button(370,button_y,50,50,PURPLE),
    Button(430,button_y,50,50,BROWN),
    Button(490, button_y, 50, 50, WHITE, "Erase", BLACK),
    Button(550, button_y, 50, 50, WHITE, "Clear", BLACK),
    Button(610, button_y, 50, 50, WHITE, "Done", BLACK)
]


gamePlaying = True

Thread(target=generateImage(prompt)).start()

while run:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if pygame.mouse.get_pressed()[0]:
            pos = pygame.mouse.get_pos()

            try:
                row, col = get_row_col_from_pos(pos)
                grid[row][col] = drawing_color
            except IndexError:
                for button in buttons:
                    if not button.clicked(pos):
                        continue

                    drawing_color = button.color
                    if button.text == "Clear":
                        grid = init_grid(ROWS, COLS, BG_COLOR)
                        drawing_color = BLACK
                    if button.text == "Done": 
                        saveImage()
                        userImg = io.imread("generatedImg.png")
                        io.imshow(userImg)
                        # generateImage(prompt)
                        run = False

    
    draw(WIN, grid, buttons)
       
run = True
pygame.Surface.fill(WIN, WHITE)
generatedImg = pygame.image.load("generatedImg.png").convert()
generatedImg =pygame.transform.scale(generatedImg,(300,300))
WIN.blit(generatedImg,(150,0))

userImg = pygame.image.load("screenshot.png").convert()
userImg =pygame.transform.scale(userImg,(400,400))
WIN.blit(userImg,(150,400))
pygame.display.update()



while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
