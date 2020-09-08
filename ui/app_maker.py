import pygame
from lib.app import App
from lib.app_city import CityApp

import json

CITY_WIDTH = 500
CITY_HEIGHT = 400

import os 
PATH_CURRENT_FILE = os.path.dirname(os.path.realpath(__file__))
PATH_FOLDER_WORLDS = os.path.join(PATH_CURRENT_FILE,"worlds/")
PATH_FILE_WORLD = os.path.join(PATH_FOLDER_WORLDS,"world.json")

class CityMakerApp(App):

    BACKGROUND_COLOR = (255,255,255)
    POINT_COLOR = (255,0,0)

    pygame.font.init() 
    FONT = pygame.font.SysFont('Comic Sans MS', 30)

    def __init__(self,window_size,path_file_save_settings):
        super(CityMakerApp,self).__init__(window_size)
        self._points = []
        self._path_file_save_settings = path_file_save_settings

        self._screen.fill(CityMakerApp.BACKGROUND_COLOR)

    def get_points(self):
        return self._points

    def on_click(self,pos): 
        self._points.append(list(pos))

    def on_suppr(self):
        self._points = self._points[:-1]

    def on_save(self):
        settings = {}
        settings["window_size"] = self._window_size
        settings["points"] = self._points

        with open(self._path_file_save_settings, 'w', encoding='utf-8') as f:
            json.dump(settings, f, ensure_ascii=False, indent=4)

    def update_surface(self):
        i = 0 
        for point in self._points: 
            pygame.draw.circle(self._screen,
                            CityMakerApp.POINT_COLOR,
                            point,
                            5)
            textsurface = CityMakerApp.FONT.render(str(i), False, (0, 0, 0))
            self._screen.blit(textsurface,point)
            i+=1

    def on_event(self,events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                self.on_click(pos)

            if event.type == pygame.KEYDOWN: 
                if(event.key == pygame.K_DELETE):
                    self.on_suppr()
                    self._screen.fill(CityMakerApp.BACKGROUND_COLOR)
                if(event.key == pygame.K_s):
                    self.on_save()
    

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((CITY_WIDTH*2, CITY_HEIGHT))

    app_maker = CityMakerApp((CITY_WIDTH,CITY_HEIGHT),PATH_FILE_WORLD)
    app_city = CityApp((CITY_WIDTH,CITY_HEIGHT))
    
    is_running = True
    while(is_running):
        events = pygame.event.get()
        for event in events: 
            if event.type == pygame.KEYDOWN: 
                if event.key == pygame.K_ESCAPE: 
                     is_running = False

        app_maker.on_event(events)
        app_city.update_points(app_maker.get_points())
        app_city.build()

        app_maker.update_surface()
        app_city.update_surface()

        screen.blit(app_maker.get_screen(), (0, 0))
        screen.blit(app_city.get_screen(), (CITY_WIDTH, 0))
        pygame.display.update()

