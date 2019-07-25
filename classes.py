import pygame

class Box:

    def __init__ (self):
        self.rect = pygame.Rect(20,20,20,20)
        self.color = pygame.Color(0,0,0)

    def colorChange(self):
        self.color = pygame.Color(0,255,0,100)

class Player:


    def __init__(self):
        self.box = Box()


    def move(self, dir):
        if dir is True:
            self.box.rect.move_ip(5,0)
        else:
            self.box.rect.move_ip(-5,0)

    def movie(self, dire):
        if dire is True:
            self.box.rect.move_ip(0,5)
        else:
            self.box.rect.move_ip(0,-5)


class Objective:
    def __init__(self):
        self.box = Box()
        self.box.color = pygame.Color(255,0,0)
        self.changed = False

    def handleCollision(self,rect):
        if self.box.rect.colliderect(rect):
            self.box.colorChange()
            ret = not self.changed
            self.changed = True
            return ret
        return False
















































