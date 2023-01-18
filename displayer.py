from constants import *
from graph import Controller
import pygame
from pygame import draw, display


class Displayer:
    def __init__(self):
        self.graphs = []

    def _draw(self):
        draw.rect(self.screen, COLOR, GRAPHS_RECT, LINE_WIDTH)
        for i in self.graphs:
            i.draw(self.screen)

    def _redraw(self):
        self.screen.fill(BACKGROUND, GRAPHS_RECT)
        self._draw()

    def save(self, filename, namehint=""):
        surface = pygame.Surface(GRAPHS_SIZE)
        print("Here")
        for i in range(GRAPHS_SIZE[0]):
            for j in range(GRAPHS_SIZE[1]):
                print((i, j))
                color = self.screen.get_at((i + GRAPHS_RECT.left, j + GRAPHS_RECT.top))
                surface.set_at((i, j), color)
        pygame.image.save(surface, filename, namehint)

    def display(self):
        init = display.get_init()
        display.init()
        if not display.get_surface() is None:
            raise RuntimeError('pygame display mode has been set')

        self.screen = display.set_mode(WINDOW_SIZE)
        self.screen.fill(BACKGROUND)
        self._draw()
        # TODO: draw buttons
        display.flip()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if GRAPHS_RECT.collidepoint(event.pos):
                        controller = None
                        for i in self.graphs:
                            if not isinstance(i, Controller):
                                continue
                            pos = event.pos
                            if i.collidepos(pos):
                                if controller is None or \
                                    (i.pos[0] - pos[0]) ** 2 + (i.pos[1] - pos[1]) ** 2 < \
                                    (controller.pos[0] - pos[0]) ** 2 + (controller.pos[1] - pos[1]) ** 2:
                                    controller = i
                        if not controller is None:
                            controller.motion(pos)
                            self._draw()
                            display.update(GRAPHS_RECT)

                    else:
                        pass

                elif event.type == pygame.MOUSEMOTION:
                    pressed = pygame.mouse.get_pressed()
                    if pressed[0]:
                        pass
                    else:
                        pass

                elif event.type == pygame.MOUSEBUTTONUP:
                    display.update(GRAPHS_RECT)

                elif event.type == pygame.QUIT:
                    self.save("螺旋线.png")
                    display.quit()
                    if init:
                        display.init()
                    return
