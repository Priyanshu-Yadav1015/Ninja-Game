import pygame
from Buttons import ScaledButton, Button
from game import Game
import os

WHITE = (255, 255, 255)
DARK_GRAY = (50, 50, 50)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
PURPLE = (255, 0, 255)
CYAN = (0, 255, 255)

LEVEL_COLORS = [RED, GREEN, BLUE, YELLOW, PURPLE, CYAN]

class level:
    def __init__(self,state,image):
        self.state = state
        self.image = image
        self.rect = self.image.get_rect()
        self.clicked = False
        self.level_no = state
    
    def draw(self, screen):
        if self.state == 0:
            screen_width, screen_height = screen.get_size()
            image_width, image_height = self.image.get_size()
            position = ((screen_width - image_width) // 2, (screen_height - image_height) // 2)
            screen.blit(self.image, position)
            self.rect.topleft = position
            action = False
            pos = pygame.mouse.get_pos()
            if self.rect.collidepoint(pos):
                if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                    action = True
                    self.clicked = True
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False
            if action:
                if(self.level_no>=0 and self.level_no<len(maps_list)):
                    Game(self.level_no).run()
            return action
           

        if self.state == 1:
            screen_width, screen_height = screen.get_size()
            image_width, image_height = self.image.get_size()
            position = ((screen_width - image_width/2), (screen_height - image_height) // 2)
            screen.blit(self.image, position)
            self.rect.topleft = position
            action = False
            pos = pygame.mouse.get_pos()
            if self.rect.collidepoint(pos):
                if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                    action = True
                    self.clicked = True
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False
            if action:
                if(self.level_no>=0 and self.level_no<len(maps_list)):
                    Game(self.level_no).run()
            return action
        if self.state == -1:
            screen_width, screen_height = screen.get_size()
            image_width, image_height = self.image.get_size()
            position = ((- image_width/2), (screen_height - image_height) // 2)
            screen.blit(self.image, position)
            self.rect.topleft = position
            action = False
            pos = pygame.mouse.get_pos()
            if self.rect.collidepoint(pos):
                if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                    action = True
                    self.clicked = True
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False
            if action:
                if(self.level_no>=0 and self.level_no<len(maps_list)):
                    Game(self.level_no).run()
            return action

    # def clicked(self,screen):
    #     action = False
    #     pos = pygame.mouse.get_pos()

	# 	#check mouseover and clicked conditions
    #     if self.rect.collidepoint(pos):
    #         if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
    #             action = True
    #             self.clicked = True

    #     if pygame.mouse.get_pressed()[0] == 0:
    #         self.clicked = False


	# 	#draw button
    #     screen.blit(self.image, self.rect)

	# 	return action
# run = True
# clock = pygame.time.Clock()
# fps = 60

# usage


def get_files_in_directory(directory):
    return sorted([f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))])

def load_and_scale_image(path, size=(300, 200)):
    img = pygame.image.load(path)
    return pygame.transform.scale(img, size)

# usage
image_files = get_files_in_directory('data/images/Levels/')
maps_list = get_files_in_directory('data/maps/')
print(image_files)

images = [load_and_scale_image(os.path.join('data/images/Levels/', f)) for f in image_files]

levels = [level(i, img) for i, img in enumerate(images)]

# while run:
#     clock.tick(fps)
#     screen.fill(WHITE)
#     for level in levels:
#         level.draw(screen)
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             run = False
#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_RIGHT:
#                 for i in levels:
#                     i.state+=1
#                     if i.state==len(levels)-1:
#                         i.state=-1
#             if event.key == pygame.K_LEFT:
#                 for i in levels:
#                     i.state-=1
#                     if i.state==-2:
#                         i.state=len(levels)-2
#     pygame.display.update()