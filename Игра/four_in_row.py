import numpy as np
import pygame
import sys
import math
import os
from pygame.locals import *

BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (255, 255, 0)
pygame.init()
pygame.key.set_repeat(200, 70)
FPS = 50
WIDTH = 750
HEIGHT = 750
STEP = 50
clock = pygame.time.Clock()
gor_count = 6
her_count = 7


def terminate():
    pygame.quit()
    sys.exit()


def load_image(name, color_key=None):
    fullname = os.path.join(name)
    try:
        image = pygame.image.load(fullname).convert()
    except pygame.error as message:
        print("Cannot load image:", name)
        raise SystemExit(message)
    if color_key is not None:
        if color_key == -1:
            color_key = image.get_at((0, 0))
        image.set_colorkey(color_key)
    else:
        image = image.convert_alpha()
    return image


def start_screen():
    intro_text = [
        "Начало игры",
        "",
        "Игра для двоих, в которой игроки сначала выбирают цвет фишек,",
        "а затем ходят по очереди, роняя фишки в ячейки",
        "вертикальной доски.",
        "Цель игры — расположить раньше противника подряд по",
        "горизонтали, вертикали или диагонали четыре фишки своего цвета. ",
    ]
    fon = pygame.transform.scale(load_image("fon2.png"), (WIDTH, HEIGHT))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 30)
    text_coord = 50
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color("black"))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                return  # начинаем игру
        pygame.display.flip()
        clock.tick(FPS)


def end_screen():
    fon = pygame.transform.scale(load_image("fon3.png"), (WIDTH, HEIGHT))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 30)
    if winning_move(board, 1):
        label = myfont.render("Выиграл первый игрок!", 1, RED)
        screen.blit(label, (40, 10))
    if winning_move(board, 2):
        label = myfont.render("Выиграл второй игрок!", 1, GREEN)
        screen.blit(label, (40, 10))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
        pygame.display.flip()
        clock.tick(FPS)


def create_board():
    board = np.zeros((gor_count, her_count))
    return board


def drop_piece(board, row, col, piece):
    board[row][col] = piece


def is_valid_location(board, col):
    return board[gor_count - 1][col] == 0


def get_next_open_row(board, col):
    for r in range(gor_count):
        if board[r][col] == 0:
            return r


def winning_move(board, piece):
    for c in range(her_count - 3):
        for r in range(gor_count):
            if (
                board[r][c] == piece
                and board[r][c + 1] == piece
                and board[r][c + 2] == piece
                and board[r][c + 3] == piece
            ):
                return True
    for c in range(her_count):
        for r in range(gor_count - 3):
            if (
                board[r][c] == piece
                and board[r + 1][c] == piece
                and board[r + 2][c] == piece
                and board[r + 3][c] == piece
            ):
                return True

    for c in range(her_count - 3):
        for r in range(gor_count - 3):
            if (
                board[r][c] == piece
                and board[r + 1][c + 1] == piece
                and board[r + 2][c + 2] == piece
                and board[r + 3][c + 3] == piece
            ):
                return True
    for c in range(her_count - 3):
        for r in range(3, gor_count):
            if (
                board[r][c] == piece
                and board[r - 1][c + 1] == piece
                and board[r - 2][c + 2] == piece
                and board[r - 3][c + 3] == piece
            ):
                return True


def draw_board(board):
    for c in range(her_count):
        for r in range(gor_count):
            pygame.draw.rect(
                screen,
                BLUE,
                (c * size_s, r * size_s + size_s, size_s, size_s),
            )
            pygame.draw.circle(
                screen,
                BLACK,
                (
                    int(c * size_s + size_s / 2),
                    int(r * size_s + size_s + size_s / 2),
                ),
                radius,
            )

    for c in range(her_count):
        for r in range(gor_count):
            if board[r][c] == 1:
                pygame.draw.circle(
                    screen,
                    RED,
                    (
                        int(c * size_s + size_s / 2),
                        height - int(r * size_s + size_s / 2),
                    ),
                    radius,
                )
            elif board[r][c] == 2:
                pygame.draw.circle(
                    screen,
                    GREEN,
                    (
                        int(c * size_s + size_s / 2),
                        height - int(r * size_s + size_s / 2),
                    ),
                    radius,
                )
    pygame.display.update()


board = create_board()
game_over = False
turn = 0
pygame.init()
size_s = 100
width = her_count * size_s
height = (gor_count + 1) * size_s
size = (width, height)
radius = int(size_s / 2 - 5)
screen = pygame.display.set_mode(size)
start_screen()
draw_board(board)
pygame.display.update()
myfont = pygame.font.SysFont("monospace", 75)
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEMOTION:
            pygame.draw.rect(screen, BLACK, (0, 0, width, size_s))
            posx = event.pos[0]
            if turn == 0:
                pygame.draw.circle(screen, RED, (posx, int(size_s / 2)), radius)
            else:
                pygame.draw.circle(screen, GREEN, (posx, int(size_s / 2)), radius)
        pygame.display.update()
        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.draw.rect(screen, BLACK, (0, 0, width, size_s))
            if turn == 0:
                posx = event.pos[0]
                col = int(math.floor(posx / size_s))
                if is_valid_location(board, col):
                    row = get_next_open_row(board, col)
                    drop_piece(board, row, col, 1)
                    if winning_move(board, 1):
                        game_over = True
            else:
                posx = event.pos[0]
                col = int(math.floor(posx / size_s))
                if is_valid_location(board, col):
                    row = get_next_open_row(board, col)
                    drop_piece(board, row, col, 2)
                    if winning_move(board, 2):
                        game_over = True
            draw_board(board)
            turn += 1
            turn = turn % 2
end_screen()
