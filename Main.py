from classes import*

import pygame
pygame.init()

player = Player()
objectives = []
objectives.append(Objective())
objectives.append(Objective())
objectives.append(Objective())
player.box.rect.center = ((500,300))
objectives[0].box.rect.center = (400,600)

screen = pygame.display.set_mode((1024,720))

def update():
    keys = pygame.key.get_pressed()
    if keys[23]:
        player.move(False)
    if keys[24]:
        player.move(True)
        for i in objectives:
            i.handleCollision(player.box.rect)

def render():
    screen.fill(pygame.Color("blue"))
    screen.fill(player.box.color,player.box.rect)
    for i in objectives:
        screen.fill(i.box.color, i.box.rect)

def main():
    while True:
        update()
        render()
        pygame.display.flip()
if __name__=="__main__":
    main()





































