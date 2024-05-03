from tkinter import *
from random import randint, choice
from time import sleep

class Field:
    def __init__(self, c, n, m, width, height):
        self.c = c
        self.n = n
        self.m = m
        self.width = width
        self.height = height
        self.a = [[choice([0, 3]) for _ in range(self.m)] for _ in range(self.n)]
        self.draw()

    def step(self):
        b = [[0] * self.m for _ in range(self.n)]

        for i in range(1, self.n - 1):
            for j in range(1, self.m - 1):
                neighbors = [self.a[i+x][j+y] for x in range(-1, 2) for y in range(-1, 2) if not (x == 0 and y == 0)]
                rock_neighbors = neighbors.count(2)
                scissors_neighbors = neighbors.count(3)
                paper_neighbors = neighbors.count(1)

                if self.a[i][j] == 2:  # Rock
                    if paper_neighbors > scissors_neighbors:
                        b[i][j] = 1  # Paper wins
                    else:
                        b[i][j] = 2  # Rock survives
                elif self.a[i][j] == 1:  # Paper
                    if scissors_neighbors > rock_neighbors:
                        b[i][j] = 3  # Scissors win
                    else:
                        b[i][j] = 1  # Paper survives
                elif self.a[i][j] == 3:  # Scissors
                    if rock_neighbors > paper_neighbors:
                        b[i][j] = 2  # Rock wins
                    else:
                        b[i][j] = 3  # Scissors survive
                else:
                    b[i][j] = 0  # Empty cell

        self.a = b
        self.draw()
        self.c.after(100, self.step)

    def draw(self):
        color_mapping = {0: "dark blue", 1: "pink", 2: "black", 3: "yellow"}
        sizen = self.width // self.n
        sizem = self.height // self.m

        for i in range(self.n):
            for j in range(self.m):
                color = color_mapping[self.a[i][j]]
                self.c.create_rectangle(i * sizen, j * sizem, (i + 1) * sizen, (j + 1) * sizem, fill=color)

root = Tk()
root.geometry("800x800")
c = Canvas(root, width=800, height=800)
c.pack()

f = Field(c, 40, 40, 800, 800)
f.step()

root.mainloop()
