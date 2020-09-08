import pygame
import abc 

class App:

    def __init__(self,window_size):
        self._window_size = window_size
        self._screen = pygame.Surface(window_size)

    def get_screen(self):
        return self._screen

    @abc.abstractmethod
    def on_event(self,events):
        pass 

    @abc.abstractmethod
    def update_surface(self):
        pass 
