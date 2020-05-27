#!/usr/bin/env python3

#Game runner, holds pygame loop

import pygame as pg
import time, copy
import SudokuSolver

BOARD = [[6, 0, 0, 1, 0, 8, 2, 0, 3],
         [0, 2, 0, 0, 4, 0, 0, 9, 0],
         [8, 0, 3, 0, 0, 5, 4, 0, 0],
         [5, 0, 4, 6, 0, 7, 0, 0, 9],
         [0, 3, 0, 0, 0, 0, 0, 5, 0],
         [7, 0, 0, 8, 0, 3, 1, 0, 2],
         [0, 0, 1, 7, 0, 0, 9, 0, 6],
         [0, 8, 0, 0, 3, 0, 0, 2, 0],
         [3, 0, 2, 9, 0, 4, 0, 0, 5]]

class Game:
    def __init__(self):
        pg.display.init()
        pg.font.init()
        self.window = pg.display.set_mode((452, 452))
        pg.display.set_caption("Sudoku")
        self.mouse_pos = ()
        self.key = None
        self.solution = SudokuSolver.runSolve(copy.deepcopy(BOARD))
        self.wrong = 0
        self.show = False

    def update_board(self):
        pg.draw.rect(self.window, (255, 255, 255), (0, 0, 450, 450))
        for i in range(9):
            for j in range(9):
                pg.draw.rect(self.window, (0, 0, 0), ((j*50), (i*50), 50, 50), 1)
                if (BOARD[i][j] != 0):
                    self.window.blit(pg.font.SysFont("Verdana", 40).render(str(BOARD[i][j]), False, (0, 0, 0)), (j*50+15,i*50+5))
        for k in range(4):
            pg.draw.line(self.window, (0, 0, 0), (0, k*150), (450, k*150), 6)
            pg.draw.line(self.window, (0, 0, 0), (k*150, 0), (k*150, 450), 6)
        if self.mouse_pos:
            pg.draw.rect(self.window, (255, 0, 0), ((self.mouse_pos[0]//50)*50+5, (self.mouse_pos[1]//50)*50+5, 40, 40), 1)
        if self.key:
            x, y = (self.mouse_pos[1]//50), (self.mouse_pos[0]//50)
            BOARD[x][y] = self.key
            if (int(BOARD[x][y]) != self.solution[x][y]):
                BOARD[x][y] = 0
                self.wrong += 1
                pg.draw.rect(self.window, (100, 100, 100), (150, 200, 150, 50))
                self.window.blit(pg.font.SysFont("Verdana", 30).render(f"{self.wrong}/3", False, (225, 0, 0)), (200, 210))
                pg.display.update()
                time.sleep(3)
                if self.wrong == 3:
                    self.show = True
            self.key = None
        pg.display.update()

    def run(self):
        running = True
        while running:
            self.update_board()
            if self.show:
                for i in range(9):
                    for j in range(9):
                        BOARD[i][j] = self.solution[i][j]
                        self.update_board()
                self.show = False
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
                if event.type == pg.MOUSEMOTION:
                    self.mouse_pos = pg.mouse.get_pos()
                if event.type == pg.KEYDOWN:
                    if chr(event.key) == " ":
                        if (BOARD == self.solution):
                            pg.draw.rect(self.window, (100, 100, 100), (150, 200, 150, 50))
                            self.window.blit(pg.font.SysFont("Verdana", 30).render("Correct!", False, (0, 255, 0)), (170, 210))
                            pg.display.update()
                            time.sleep(3)
                    elif chr(event.key) != 0:
                        self.key = chr(event.key)

        pg.quit()
        quit()

game = Game()
game.run()
