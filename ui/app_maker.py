import pygame
from lib.app import App
from lib.city import CityApp

class CityMakerApp(App):

    BACKGROUND_COLOR = (255,255,255)
    POINT_COLOR = (255,0,0)

    pygame.font.init() 
    FONT = pygame.font.SysFont('Comic Sans MS', 30)

    def __init__(self,window_size):
        super(CityMakerApp,self).__init__(window_size)
        self._points = []

        self._screen.fill(CityMakerApp.BACKGROUND_COLOR)

    def get_points(self):
        return self._points

    def on_click(self,pos): 
        self._points.append(list(pos))

    def on_suppr(self):
        self._points = self._points[:-1]

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
    

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((1000, 400))

    app = CityMakerApp((500,400))
    app_city = CityApp((500,400))
    
    while(True):
        env = pygame.event.get()
        
        app.on_event(env)
       
        app_city.update_points(app.get_points())
        app_city.build()

        app.update_surface()
        app_city.update_surface()

        screen.blit(app.get_screen(), (0, 0))
        screen.blit(app_city.get_screen(), (500, 0))
        pygame.display.update()

