#!c:\\python27\python.exe
import pyglet
from pyglet import window

#Loaded the GIF image in this section
animation = pyglet.image.load_animation('Maya_GUI_Image\giphy.gif')
animSprite = pyglet.sprite.Sprite(animation)

w = animSprite.width
h = animSprite.height

#created GUI window and defined its size, Title & type
window = pyglet.window.Window(480,480,"MAYA Artificial Intelligence", style=window.Window.WINDOW_STYLE_DIALOG)

#Created an Icon for the Window
icon = pyglet.image.load('Maya_GUI_Image\AI1.png')
window.set_icon(icon)

@window.event
def on_draw():
    window.clear()
    animSprite.draw()

pyglet.app.run()
