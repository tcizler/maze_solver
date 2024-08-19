from time import sleep
from geometry import Cell,Point
import random


class Maze:
    def __init__(self, x, y, num_rows, num_cols, cell_size_y,cell_size_x,win):
        self.x = x
        self.y = y
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self._create_cells()
        
    def _create_cells(self):
        self._cells = []
        for row in range(0,self.num_rows):
            self._cells.append([])
            for col in range(0,self.num_cols):
                self._cells[row].append(Cell(
                    Point(self.x + self.cell_size_x * col,self.y + self.cell_size_y * row),
                    Point(self.x + self.cell_size_x * (col + 1),self.y + self.cell_size_y * (row + 1))
                    ))
        self._draw_cells()
    
    def _draw_cells(self):
        for row in range(0,len(self._cells)):
            for cell in range(0,len(self._cells[row])):
                self._cells[row][cell].draw(self.win.canvas,"black")
        self.animate()
    
    def animate(self):
        print("stinky")

        self.win.redraw()

        self._cells[random.randint(0,self.num_rows - 1)][random.randint(0,self.num_cols - 1)].has_bottom_wall = False
        sleep(0.05)
        self._draw_cells()
        
        
        
        