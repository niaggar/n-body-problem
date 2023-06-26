import logging
import pyglet

from App import MainWindow

logging.basicConfig(filename='.\\logs\\main.log', filemode='w', level=logging.DEBUG)

window = MainWindow(fullscreen = True)

pyglet.app.run()
