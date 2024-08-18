from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self,width,height):
        self.width = width
        self.height = height
        self.root = Tk()
        self.root.title = "Maze Solver"
        self.root.protocol("WM_DELTE_WINDOW",self.close)
        self.canvas = Canvas(self.root, width = width, height = height, bg = "white")
        self.canvas.pack()
        self.running = False

    def redraw(self):
        self.root.update_idletasks()
        self.root.update()
    
    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()
    
    def close(self):
        self.running = False

    def draw_line(self,line,fill_color):
        line.draw(self.canvas, fill_color)
