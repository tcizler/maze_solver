from window import Window
from geometry import Line,Point,Cell

window = Window(800,600)
window.draw_line(Line(Point(0,0),Point(100,100)),"red")

cell = Cell(Point(125,125),Point(175,175),False)
cell.draw(window.canvas,"yellow")

cell2 = Cell(Point(200,200),Point(250,250),False,False)
cell2.draw(window.canvas,"green")

cell3 = Cell(Point(275,275),Point(325,325))
cell3.draw(window.canvas,"red")

window.wait_for_close()