from Models import Dimension2D


class Derivate:
    modelFunction = None
    precision = 0.01

    def __init__(self, modelFunction, precision=0.01):
        self.modelFunction = modelFunction
        self.precision = precision
    
    def partial(self, point: Dimension2D) -> Dimension2D:
        dx = self.precision
        dy = self.precision

        x0 = self.modelFunction.calculate(point)
        point.x += dx
        xh = self.modelFunction.calculate(point)
        derivateX = (xh - x0) / dx
        point.x -= dx

        y0 = self.modelFunction.calculate(point)
        point.y += dy
        yh = self.modelFunction.calculate(point)
        derivateY = (yh - y0) / dy
        point.y -= dy

        return Dimension2D(derivateX, derivateY)
