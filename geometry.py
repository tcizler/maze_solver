class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

class Line:
    def __init__(self,start,end):
        self.start = start
        self.end = end

    def draw(self,canvas,fill_color):
        #print(canvas,fill_color)
        canvas.create_line(
            self.start.x, self.start.y, self.end.x, self.end.y, fill=fill_color, width = 2
        )

class Cell:
    def __init__(self,topleft,bottomright,wall_right=True,wall_left=True,wall_top=True,wall_bottom=True):
        self._topleft = topleft
        self._bottomright = bottomright
        self.wall_right = wall_right
        self.wall_left = wall_left
        self.wall_top = wall_top
        self.wall_bottom = wall_bottom

    def draw(self,canvas,fill_color):
        if self.wall_top:
            canvas.create_line(
                self._topleft.x, self._topleft.y, self._bottomright.x, self._topleft.y, fill=fill_color, width = 2
            )
        if self.wall_left:
            canvas.create_line(
                self._topleft.x, self._topleft.y, self._topleft.x, self._bottomright.y, fill=fill_color, width = 2
            )
        if self.wall_right:
            canvas.create_line(
                self._bottomright.x, self._topleft.y, self._bottomright.x, self._bottomright.y, fill=fill_color, width = 2
            )
        if self.wall_bottom:
            canvas.create_line(
                self._topleft.x, self._bottomright.y, self._bottomright.x, self._bottomright.y, fill=fill_color, width = 2
            )