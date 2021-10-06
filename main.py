import sys
import math
import random
import time

from pyglet import image
from pyglet.gl import *
from pyglet.graphics import TextureGroup
from pyglet.window import key, mouse


# Data Structures
class GameScreen():
    """This node is the game screen which minecraft is played in"""
    window = pyglet.window.Window(1280, 720, resizable=False)
    window.set_caption('CrazyJuniors-Minecraft')

    def __init__(self):
        pass

    def __str__(self):
        return "Game Screen"

    def get_game_screen(self):
        return self.window


class Cube():
    pass


class Player():
    pass


class Camera():
    pass


class Terrain():
    pass


class SkyDome():
    pass


class Fog():
    pass


class BackgroundMusic():
    pass



# Algorithms
def create_game_screen():
    pass


def mouse_not_moving_from_screen():
    pass


def walking():
    pass


def jumping():
    pass


def first_person_camer():
    pass


def putting_cube():
    pass


def removing_cube():
    pass


def keyboard_texture_switch():
    pass


def play_background_music():
    pass


def setup():
    pass



def main():
    new_window = GameScreen()


    pyglet.app.run()


if __name__ == '__main__':
    main()
