import copy
import pygame

from .app import App
from .road import Road

class CityApp(App):

    ROAD_COLOR = (100,100,100)
    ROAD_SIZE = 20
    ROAD_LINE_SIZE = 2
    ROAD_LINE_COLOR = (255,255,255)
    BACKGROUND_COLOR = (0, 153, 38)

    def __init__(self,window_size,points_initial=[]):
        super(CityApp,self).__init__(window_size)
        self._points_initials = points_initial
        self._roads = []
        self._roads_points = []

        self._screen.fill(CityApp.BACKGROUND_COLOR)

    def update_points(self,points):
        self._points_initials = points

    def build(self):
        if(self._points_initials == None or len(self._points_initials) == 0):
            return 
        self._roads = []
        self._roads_points = []
        previous_point = None
        points_initials_close = copy.copy(self._points_initials) + [self._points_initials[0]]
        for point in points_initials_close:
            if(previous_point != None):
                p_to_ax1 = copy.copy(previous_point)
                p_to_ax1[0] = point[0]
                p_to_ax2 = copy.copy(p_to_ax1)
                p_to_ax2[1] = point[1]
                self._roads.append(Road(previous_point,p_to_ax1))
                self._roads.append(Road(p_to_ax1,p_to_ax2))
                self._roads_points += [previous_point,p_to_ax1,p_to_ax2]
            previous_point = point

    def update_surface(self):
        self._screen.fill(CityApp.BACKGROUND_COLOR)
        if(self._roads_points == None or len(self._roads_points) <= 1): 
            return

        for point in self._roads_points:
            pygame.draw.circle(self._screen,
                               CityApp.ROAD_COLOR,
                               point,
                               int(CityApp.ROAD_SIZE/2))

        pygame.draw.lines(self._screen,
                         CityApp.ROAD_COLOR,
                         False,
                         self._roads_points,
                         CityApp.ROAD_SIZE)

        pygame.draw.lines(self._screen,
                          CityApp.ROAD_LINE_COLOR,
                          False,
                          self._roads_points,
                          CityApp.ROAD_LINE_SIZE)

