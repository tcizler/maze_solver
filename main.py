from window import Window
from geometry import Line,Point,Cell
from maze import Maze

window = Window(800,600)
maze = Maze(25, 25, 20, 20, 25, 25, window)


window.wait_for_close()