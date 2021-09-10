import pygame


class Button:
    def __init__(self, screen, gui_font, text, width, height, pos):
        self.screen = screen
        self.pressed = False
        self.top_rect = pygame.Rect(pos, (width, height))
        self.top_color = "#475F77"
        self.text_surface = gui_font.render(text, True, "#FFFFFF")
        self.text_rect = self.text_surface.get_rect(center=self.top_rect.center)

    def draw(self):
        pygame.draw.rect(self.screen, self.top_color, self.top_rect)
        self.screen.blit(self.text_surface, self.text_rect)
        return self.if_clicked()

    def if_clicked(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.top_rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0]:
                self.pressed = True
            else:
                if self.pressed:
                    self.pressed = False
                    return True

