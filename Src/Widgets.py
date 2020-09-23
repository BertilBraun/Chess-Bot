
import pyglet
from pyglet import shapes
from pyglet.window import mouse

class Button:
    def __init__(self, name, x, y, w, h, color=(150, 150, 150), on_click=None, border=2, borderColor=(0, 0, 0)): 
        self.background = shapes.Rectangle(x - w // 2, y - h // 2, w, h, color)

        self.label = pyglet.text.Label(name,
                          font_name='Times New Roman',
                          font_size=36,
                          x=x, y=y,
                          anchor_x='center', anchor_y='center')
        self.on_click = on_click

        self.minx = x - w // 2
        self.miny = y - h // 2
        self.maxx = x + w // 2
        self.maxy = y + h // 2

        self.boarderOfSelectables = []
        self.boarderOfSelectables.append(pyglet.shapes.Line(self.minx, self.miny, self.maxx, self.miny, border, borderColor))
        self.boarderOfSelectables.append(pyglet.shapes.Line(self.minx, self.miny, self.minx, self.maxy, border, borderColor))
        self.boarderOfSelectables.append(pyglet.shapes.Line(self.minx, self.maxy, self.maxx, self.maxy, border, borderColor))
        self.boarderOfSelectables.append(pyglet.shapes.Line(self.maxx, self.miny, self.maxx, self.maxy, border, borderColor))

    def draw(self):
        self.background.draw()
        self.label.draw()
        for border in self.boarderOfSelectables:
            border.draw()
        
    def onMouseClick(self, x, y, button):
        if x >= self.minx and x <= self.maxx and y >= self.miny and y <= self.maxy and button == mouse.LEFT:
            self.on_click()