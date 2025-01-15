import pygame

WIDTH, HIGHT = 800, 500 

WIN = pygame.display.set_mode((WIDTH, HIGHT))

pygame.display.set_caption("Tic-Tac-Toe")

WHITE = (255, 255, 255)
FPS = 60

pygame.init()

font = pygame.font.Font(None, 200)

def generate_x():
    text = font.render("X", True, (0,0,0))
    return text

def generate_O():
    text = font.render("O", True, (0,0,0))
    return text



def draw_grid():
    pygame.draw.line(WIN,(0,0,0), (200, 180), (590, 180))
    pygame.draw.line(WIN,(0,0,0), (200, 310), (590, 310))
    pygame.draw.line(WIN,(0,0,0), (330, 50), (330, 440))
    pygame.draw.line(WIN,(0,0,0), (460, 50), (460, 440))



def draw_window(moves1, moves2, map, win, draw):
    WIN.fill(WHITE)
    draw_grid()

    for i in moves1:
        WIN.blit(generate_x(), map[i])
        
            
    for j in moves2:
        WIN.blit(generate_O(), map[j])


    if win == 1:
        font_1 = pygame.font.Font(None, 40)
        text = font_1.render("Player 1 WINS!!!", None, (0,0,0))
        text2 = font_1.render("Press Enter to Replay", None, (0,0,0))
        
    if win == 2:
        font_1 = pygame.font.Font(None, 40)
        text = font_1.render("Player 2 WINS!!!", None, (0,0,0))
        text2 = font_1.render("Press Enter to Replay", None, (0,0,0))

    if win:
        WIN.blit(text, (10,10))
        WIN.blit(text2, (10, 450))

    if draw and not win:
        font_1 = pygame.font.Font(None, 40)
        text = font_1.render("Draw", None, (0,0,0))
        text2 = font_1.render("Press Enter to Replay", None, (0,0,0))
        WIN.blit(text, (10,10))
        WIN.blit(text2, (10,450))
        
    pygame.display.update()



GRID_ROWS, GRID_COLS = 3, 3
CELL_WIDTH, CELL_HEIGHT = 130, 130
GRID_START_X, GRID_START_Y = 200, 50

rects = [
    pygame.Rect(
        GRID_START_X + CELL_WIDTH*(i % GRID_COLS),
        GRID_START_Y + CELL_HEIGHT*(i // GRID_ROWS),  #list of Rect-objs 
        CELL_WIDTH,                                   #corresponding to
        CELL_HEIGHT                                   #each cell in grid
    )
    for i in range(GRID_ROWS*GRID_COLS)
]

#dictionary mapping the numbers representing each cell to corresponding Rect
positions = { i + 1 : rect.topleft for i, rect in enumerate(rects)} 
   


def grid():
    grid = [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]
    return grid

def assign_values_to(grid, moves1, moves2):
     win = {
        1 : [0,0],
        2 : [0,1],
        3 : [0,2],
        4 : [1,0],
        5 : [1,1],
        6 : [1,2],
        7 : [2,0],
        8 : [2,1],
        9 : [2,2]
     }

     for i in moves1:
        coordinates = win[i]
        grid[coordinates[0]][coordinates[1]] = 'X'

     for j in moves2:
        coordinates = win[j]
        grid[coordinates[0]][coordinates[1]] = 'O'

    
def winner(grid, count):
    
    if( (grid[0][0] == grid[0][1] and grid[0][1] == grid[0][2]) or
        (grid[1][0] == grid[1][1] and grid[1][1] == grid[1][2]) or
        (grid[2][0] == grid[2][1] and grid[2][1] == grid[2][2]) or
        (grid[0][0] == grid[1][0] and grid[1][0] == grid[2][0]) or
        (grid[0][1] == grid[1][1] and grid[1][1] == grid[2][1]) or
        (grid[0][2] == grid[1][2] and grid[1][2] == grid[2][2]) or
        (grid[0][0] == grid[1][1] and grid[1][1] == grid[2][2]) or
        (grid[0][2] == grid[1][1] and grid[1][1] == grid[2][0]) ):

        if count%2 == 0:
            return 2
        else:
            return 1
        
    return 0

def draw(grid):
    for i in grid:
        for j in i:
            if j == 'X' or j == 'O':
                continue
            else:
                return 0
            
    return 1
    
    

def main():
    clock = pygame.time.Clock()
    running = True
    
    #store_coordinates()
    player1_moves = []
    player2_moves = []

    matrix = grid()

    def reset_game():
        nonlocal player1_moves, player2_moves, matrix, count
        count = 0
        player1_moves = []
        player2_moves = []
        matrix = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]

    
    
    count = 0
    

    while running:
        clock.tick(FPS)
        

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    reset_game()


            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos
                count += 1
                if event.button == 1:

                    for idx, rect in enumerate(rects, start=1):
                        if rect.collidepoint(pos) and idx not in player1_moves + player2_moves:
                            (player2_moves if count%2 == 0 else player1_moves).append(idx)
                            break



        assign_values_to(matrix, player1_moves, player2_moves)
        win = winner(matrix, count)

        draw_check = draw(matrix)


        draw_window(player1_moves, player2_moves, positions, win, draw_check)

        
            
        

    pygame.quit()


if __name__ == "__main__":
    main()
