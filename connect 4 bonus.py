import numpy as np
import pygame
import sys
import math

colour1 = (170,0,255)
colour2 = (0,0,0)
colour3 = (255,0,0)
colour4 = (254,255,0)
turn = 0

colum = 7
raw = 6

def graphic(board):
    for c in range(colum):
        for r in range(raw):
               pygame.draw.rect(screen,colour1,(c*win_size, r*win_size+win_size,win_size,win_size))
               pygame.draw.circle(screen,colour2,(int(c*win_size+ win_size/2),int(r*win_size+win_size+win_size/2)),radius)


    for c in range(colum):
        for r in range(raw):
           if board[r][c] == 1:
                pygame.draw.circle(screen,colour3,(int(c*win_size+win_size/2),high - int(r*win_size+win_size/2)),radius)
           elif board[r][c] == 2:
               pygame.draw.circle(screen,colour4,(int(c*win_size+win_size/2),high - int(r*win_size+win_size/2)),radius)
    pygame.display.update()

def is_empty(board,colum,raw) :
    global Player_raw
    Player_raw = 0
    for i in range(raw):
       if board[i][colum] == 0:
           Player_raw = i
           return True
    return False
def flip_board(board):
    print(np.flip(board, 0))

def is_Win(board ,Player_raw, Player_col, sign):
    global Player_score
    Player_score = 0
    R = Player_raw
    C = Player_col

    while C < 7 :
           if board[R][C] == sign :
               Player_score+=1
               C+=1
           elif board[R][C] != sign :
               break
           if Player_score == 4:
                return True

    Player_score = 0
    R = Player_raw
    C = Player_col
    while C >= 0 :
           if board[R][C] == sign :
               Player_score+=1
               C-=1
           elif board[R][C] != sign :
               break
           if Player_score == 4:
                return True

    Player_score = 0
    R = Player_raw
    C = Player_col
    while R < 6:
        if board[R][C] == sign:
            Player_score += 1
            R += 1
        elif board[R][C] != sign:
            break
        if Player_score == 4:
            return True

    Player_score = 0
    R = Player_raw
    C = Player_col
    while R >= 0:
        if board[R][C] == sign:
            Player_score += 1
            R -= 1
        elif board[R][C] != sign:
            break
        if Player_score == 4:
            return True
    Player_score = 0
    R = Player_raw
    C = Player_col
    while R < 6 and C < 7:
        if board[R][C] == sign:
            Player_score += 1
            R += 1
            C += 1
        elif board[R][C] != sign:
            break
        if Player_score == 4:
            return True

    Player_score = 0
    R = Player_raw
    C = Player_col
    while R >= 0 and C >= 0:
        if board[R][C] == sign:
            Player_score += 1
            R -= 1
            C -= 1
        elif board[R][C] != sign:
            break
        if Player_score == 4:
            return True
    Player_score = 0
    R = Player_raw
    C = Player_col
    while R >= 0 and C < 7:
        if board[R][C] == sign:
            Player_score += 1
            R -= 1
            C += 1
        elif board[R][C] != sign:
            break
        if Player_score == 4:
            return True
    Player_score = 0
    R = Player_raw
    C = Player_col
    while R < 6 and C >= 0:
        if board[R][C] == sign:
            Player_score += 1
            R += 1
            C -= 1
        elif board[R][C] != sign:
            break
        if Player_score == 4:
            return True

Sign1=1
Sign2=2

board = np.zeros((6,7))

print(board)

pygame.init()

win_size = 100

wide = colum * win_size
high = (raw+1) * win_size
varp = 1
size = (wide,high)
radius = int(win_size/2 - 5)
screen = pygame.display.set_mode(size)
graphic(board)
pygame.display.update()
playing = 0
mmfont = pygame.font.SysFont("arial", 75)

while playing == 0 :
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.MOUSEMOTION:
                pygame.draw.rect(screen,colour2,(0, 0, wide,win_size))
                xpos = event.pos[0]
                if turn == 0:
                    pygame.draw.circle(screen,colour3,(xpos, int(win_size/2)), radius)
                else:
                    pygame.draw.circle(screen,colour4,(xpos, int(win_size/2)), radius)
            pygame.display.update()
            varp = bool(1)

            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.draw.rect(screen, colour2, (0, 0, wide, win_size))
                if turn == 0 :
                    xpos = event.pos[0]
                    Player1_col = int(math.floor(xpos/win_size))
                    if is_empty(board,Player1_col,raw):
                        board[Player_raw][Player1_col] = "1"
                        graphic(board)
                        turn = 1
                    else:
                        print("this Place is not available try again P1")
                        continue
                    if is_Win(board,Player_raw,Player1_col,Sign1):
                         printing = mmfont.render("Player 1 wins!!", varp, colour3)
                         screen.blit(printing, (40, 10))
                         flip_board(board)
                         pygame.display.update()
                         playing = 1
                    flip_board(board)

                else:
                    xpos = event.pos[0]
                    Player2_col = int(math.floor(xpos / win_size))
                    if is_empty(board, Player2_col, raw):
                        board[Player_raw][Player2_col] = "2"
                        graphic(board)
                        turn = 0
                    else:
                        print("this Place is not available try again P2")
                        continue
                    if is_Win(board, Player_raw, Player2_col, Sign2):
                        flip_board(board)
                        label = mmfont.render("Player 2 wins!!", varp, colour4)
                        screen.blit(label, (40, 10))
                        pygame.display.update()
                        playing = 2
                    flip_board(board)

if playing != 0 :
    pygame.time.wait(2000)
