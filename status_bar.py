import pygame

MARGIN = 10
HEIGHT_RATIO = 0.1
WIDTH = 10
BG_COLOR = (0, 0, 0)
FG_COLOR = (100, 151, 177)


class StatusBar:
    def __init__(self, track_size, track_index):
        self.track_size = track_size
        self.track_index = track_index
        self.left = track_size['width'] - MARGIN - WIDTH
        self.top = track_size['height'] * HEIGHT_RATIO
        self.height = track_size['height']*(1 - 2*HEIGHT_RATIO)

    def update(self, ratio, screen):
        pygame.draw.rect(screen, BG_COLOR, (self.left,
                                            self.top, WIDTH, self.height))
        status_height = ratio * self.height
        status_top = self.top + (1 - ratio) * self.height
        pygame.draw.rect(screen, FG_COLOR, (self.left,
                                            status_top, WIDTH, status_height))
