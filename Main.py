from classes import Box, Objective, Player
import sys, pygame
import random

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((600,600))
player = Player()
counter = 0
timer_sec = 0
timer_frame = 0
timer_print = pygame.font.SysFont("Times New Roman", 24)
objectives = []
for i in range(50):
    objectives.append(Objective())
player.box.rect.center = ((20,240))

for i in objectives:
    i.box.rect.center = (random.randint(0,575),random.randint(0,575))

def update():
    pygame.event.pump()
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT]:
        player.move(False)
    elif key[pygame.K_RIGHT]:
        player.move(True)

def update2():
    global counter
    pygame.event.pump()
    key = pygame.key.get_pressed()
    if key[pygame.K_DOWN]:
        player.movie(True)
    elif key[pygame.K_UP]:
        player.movie(False)
    for i in objectives:
        if i.handleCollision(player.box.rect):
            counter += 1

def update3():
    global timer_frame, timer_sec
    if counter < 50:
        timer_frame += 1
        if timer_frame >= 60:
            timer_sec += 1
            timer_frame = 0




def render():
    screen.fill(color=pygame.Color("blue"))
    screen.fill(player.box.color,player.box.rect)
    for i in objectives:
        screen.fill(i.box.color, i.box.rect)
    screen.blit(timer_print.render((str(timer_sec)), 1, (255, 255, 0, 255)), (0, 0))


def main():
    while True:
        clock.tick(60)
        update()
        update2()
        update3()
        render()
        pygame.display.flip()
if __name__=="__main__":
    main()













