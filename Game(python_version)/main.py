import pygame

from system.keyboard import controller
from system.tank import Tank


class GameWindow:
    def __init__(self):
        self.path_to_logo = '..\images\icon.png'
        self.display_size = (1000, 1000)
        self.background_color = (105, 105, 105)
        self.title = 'Tanchiki'
        self.status_run = True
        self.clock = pygame.time.Clock()
        self.fps = 60
        self.screen = None
        self.objects = list()

    def set_icon(self):
        icon_img = pygame.image.load(self.path_to_logo)
        pygame.display.set_icon(icon_img)

    def create_window(self):
        # display size and background color
        self.screen = pygame.display.set_mode(self.display_size)
        self.screen.fill(self.background_color)

        # Title and FLIP
        pygame.display.set_caption(self.title)
        pygame.display.flip()

    def build(self):
        while self.status_run:
            for event in pygame.event.get():

                # Quit buttons
                if event.type == pygame.QUIT:
                    self.status_run = False
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    self.status_run = False

                # User action
                if event.type == pygame.KEYDOWN:
                    for obj in self.objects:
                        self.screen.fill(self.background_color)
                        controller(event, obj)

            # Display update
            pygame.display.update()
            self.clock.tick(self.fps)

    def run(self):
        # Window configure
        self.set_icon()
        self.create_window()
        self.screen = pygame.display.set_mode(self.display_size)
        self.screen.fill(self.background_color)

        # Game configure
        self.create_player()
        self.build()

    def create_player(self):
        player = Tank(self.screen)
        self.objects.append(player)


if "__main__" == __name__:
    game = GameWindow()
    game.run()
