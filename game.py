"""
Game Instance
"""

import pygame

class Game(object):
    # DEFAULT SETTINGS
    SCREEN_DIMENSION = (1280, 720)
    TITLE = "Chess"
    FPS_LIMIT = 60

    def __init__(self):
        # PyGame Window Configuration
        self.init_window()


        self.running = True

    def init_window(self):
        pygame.display.init()
        pygame.display.set_caption(Game.TITLE)
        
        self.screen = pygame.display.set_mode(Game.SCREEN_DIMENSION)
        self.clock = pygame.time.Clock()

    def show_menu(self):
        pass

    def start_game(self):
        pass

    def show_end_screen(self):
        pass


    # ENGINE FUNCTIONS
    def handle_events(self):
        for evnt in pygame.event.get():
            if evnt.type == pygame.QUIT:
                self.running = False
        pass

    def process_gameplay(self):
        pass

    def render(self):
        pass

    def run(self):
        while self.running:
            self.handle_events()
            self.process_gameplay()
            self.render()
        pygame.quit()
