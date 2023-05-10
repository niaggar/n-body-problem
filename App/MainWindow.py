import pyglet
import logging
from pyglet.window import key
from pyglet import shapes

from Models import Body, Dimension2D, Bounds
from Methods import Potencial, Verlet
from Utils import create_random_bodies


class MainWindow(pyglet.window.Window):
    NUMBER_OF_BODIES = 5
    bodies: list[Body] = []
    bounds: Bounds = None
    potencial: Potencial = None
    verlete: Verlet = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.set_minimum_size(800, 600)
        self.set_caption("N-Body Simulation")

        window_size = self.get_size()
        self.bounds = Bounds(Dimension2D(0, 0), Dimension2D(window_size[0], window_size[1]))
        self.potencial = Potencial(G = 10000)
        self.bodies = create_random_bodies(self.NUMBER_OF_BODIES, self.bounds)
        self.verlete = Verlet(self.bodies, 1/100, self.bounds, self.potencial)
        self.logger = logging.getLogger("main")

    def update(self, dt):
        self.bodies = self.verlete.update()
    
    def on_draw(self):
        self.clear()

        for body in self.bodies:
            main_bathc = shapes.Batch()
            color = body.color

            force = body.aceleration.scale(0.8)
            if force.magnitude() > 200:
                force = force.normalize().scale(200)
            force_line = shapes.Line(x=body.position.x, y=body.position.y, x2=body.position.x + force.x, y2=body.position.y + force.y, width=1, color=color, batch=main_bathc)
            force_point = shapes.Circle(x=body.position.x + force.x, y=body.position.y + force.y, radius=3, color=(255, 0, 0), batch=main_bathc)

            path_lines = []
            for i in range(len(body.path) - 1):
                point = body.path[i]
                next_point = body.path[i + 1]
                path_line = shapes.Line(x=point[0], y=point[1], x2=next_point[0], y2=next_point[1], width=3, color=color, batch=main_bathc)
                path_line.opacity = 80
                path_lines.append(path_line)

            body_circle = shapes.Circle(x=body.position.x, y=body.position.y, radius=body.radius, color=color)
            main_bathc.draw()
            body_circle.draw()

    def on_key_press(self, symbol, modifiers):
        if symbol == key.ENTER:
            pyglet.clock.schedule_interval(self.update, 1/60.)
        elif symbol == key.SPACE:
            pyglet.clock.unschedule(self.update)
        elif symbol == key.R:
            self.bodies = create_random_bodies(self.NUMBER_OF_BODIES, self.bounds)
            self.verlete = Verlet(self.bodies, 1/100, self.bounds, self.potencial)

            
    
    
