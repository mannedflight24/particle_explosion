import pygame
import sys
import settings


class ParticleExplosion:
    def __init__(self):
        # initialize parameters
        self.settings = settings.Settings()
        self.width = self.settings.WIDTH
        self.height = self.settings.HEIGHT
        self.bg_color = self.settings.bg_color
        # initialize the screen
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Particle Explosion")
        self.screen_rect = self.screen.get_rect()

    def on_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def on_loop(self):
        pass

    def on_render(self):
        self.screen.fill(self.bg_color)
        pygame.display.flip()

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):

        while True:
            self.on_event()
            self.on_loop()
            self.on_render()
        self.on_cleanup()


if __name__ == "__main__":
    pe = ParticleExplosion()
    pe.on_execute()
