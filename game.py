"""
Game Instance
"""

import pygame

from board import Board

class Game(object):
    # DEFAULT SETTINGS
    SCREEN_DIMENSION = (1200, 800)
    TITLE = "Chess"
    FPS_LIMIT = 60

    def __init__(self):
        # PyGame Window Configuration
        self.__init_window()


        self.running = True
        self.start_game()

    def __init_window(self):
        pygame.display.init()
        pygame.display.set_caption(Game.TITLE)
        
        self.screen = pygame.display.set_mode(Game.SCREEN_DIMENSION)
        self.clock = pygame.time.Clock()

    def show_menu(self):
        pass

    def start_game(self):
        self.board = Board()

    def show_end_screen(self):
        pass


    # ENGINE FUNCTIONS
    def handle_events(self):
        for evnt in pygame.event.get():
            if evnt.type == pygame.QUIT:
                self.running = False

    def process_gameplay(self):
        pass

    def render(self):
        # Draw Window Background
        self.screen.fill((236, 229, 221))

        # Draw Board
        self.board.render(self.screen)

        # Draw Highlight-Colors

        # Draw Pieces

        # Update Screen Display
        pygame.display.update()

    def run(self):
        while self.running:
            self.handle_events()
            self.process_gameplay()
            self.render()
        pygame.quit()
