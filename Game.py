import pygame
import random

pygame.init()
size = (800, 600)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
x = -1
y = -1
klik = 0
points = 0
qa = 0
play = 0
xy = (-1, -1)
ochki = 0
poloska = 400
poloska_g = 250
poloska_r = 0
end = 0
shi = 50
vi = 50
tick_per_second = 40
running = True
ga_ov = pygame.image.load("game_over.png").convert_alpha()
start = pygame.image.load("START.png").convert_alpha()

dzin = pygame.mixer.Sound('dzin.wav')
pygame.mixer.music.load('fon1.mp3')
pygame.mixer.music.play(-1)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEMOTION:
            pass
        if event.type == pygame.MOUSEBUTTONDOWN:
            xy = event.pos
            if play == 1:
                klik = 1
        if event.type == pygame.MOUSEBUTTONUP:
            pass
        if event.type == pygame.KEYUP:
            if play == 0:
                play = 1
            if play == 3:
                x = -1
                y = -1
                klik = 0
                points = 0
                qa = 0
                play = 0
                xy = (-1, -1)
                ochki = 0
                poloska = 400
                poloska_g = 250
                poloska_r = 0
                end = 0
                shi = 50
                vi = 50
                tick_per_second = 40
                running = True


    if play == 0:
        screen.fill((222, 0, 0))
        screen.blit(start, (0, 0))

    elif play == 1:
        screen.fill((255, 255, 255))
        if qa == 0:
            qa = 1
            x = random.choice(range(100, 650))
            y = random.choice(range(100, 450))
            speed_x = (random.choice(range(0, 2)) - 1)
            speed_y = (random.choice(range(0, 2)) - 1)
            kvadrat = random.choice(range(0, 6))
            if points > 2000:
                shi = random.choice(range(20, 51))
                vi = random.choice(range(20, 51))
        if kvadrat == 0:
            pygame.draw.rect(screen, (100, 100, 255), (x, y, shi, vi), 0)
        elif kvadrat == 1:
            pygame.draw.rect(screen, (255, 100, 100), (x, y, shi, vi), 0)
        else:
            pygame.draw.rect(screen, (100, 255, 100), (x, y, shi, vi), 0)
        if points > 5000:
            x = x + speed_x
            y = y + speed_y

    if x <= xy[0] <= x + shi and y <= xy[1] <= y + vi and klik == 1:
        dzin.play()
        tick_per_second = tick_per_second + 2
        if kvadrat == 0:
            points = (points * 2 * (poloska / 400)) // 1
        if kvadrat == 1:
            if poloska < 100:
                points = (points - ochki + (ochki * (poloska / 400))) // 1
            else:
                points = points + ochki
        if kvadrat > 1:
            ochki = ochki + 1
            points = points + ochki

        qa = 0
        klik = 0
        poloska = 400
        poloska_g = 250
        poloska_r = 0

    elif klik == 1 and play == 1:
        play = 2
        pygame.mixer.music.stop()

    if play == 1:
        text = pygame.font.Font("freesansbold.ttf", 20)
        text = text.render("{}".format(int(points)), 1, (250, 150, 0))
        screen.blit(text, (0, 0))

        poloska = poloska - 1
        poloska_g = poloska_g - 0.625
        poloska_r = poloska_r + 0.625
        if poloska == 0:
            play = 2
        pygame.draw.rect(screen, (poloska_r, poloska_g, 0), (200, 570, poloska, 30), 0)

    if play == 2:
        if end == 0:
            tick_per_second = 40
            pygame.mixer.music.load('end.mp3')
            pygame.mixer.music.play()
            end = 1
            screen.blit(ga_ov, (0, 0))
            text = pygame.font.Font("freesansbold.ttf", 48)
            text = text.render("Ваш результат: {}".format(int(points)), 1, (0, 0, 0))
            screen.blit(text, (140, 450))
            top = open('top.txt', 'a')
            top.write(str(int(points)) + '\n')
            top.close()
        end = end + 1
        if end == 120:
            play = 3
            end = 0
    if play == 3:
        if end == 0:
            top = open('top.txt')
            to = top.read().split()
            for i in range(len(to)):
                to[i] = int(to[i])
            to.sort()
            top.close()
        screen.fill((255, 255, 255))
        for j in range(5):
            text = pygame.font.Font("freesansbold.ttf", 30)
            text = text.render("{} место:  {}".format(j + 1, to[-j - 1]), 1, (0, 0, 0))
            screen.blit(text, (200, 70 * j + 30))
        text = pygame.font.Font("freesansbold.ttf", 30)
        text = text.render("Ваше место - {}".format(len(to) - to.index(points)), 1, (250, 100, 0))
        screen.blit(text, (200, 350))

        text = pygame.font.Font("freesansbold.ttf", 25)
        text = text.render("Нажмите любую клавишу, чтобы начать заново", 1, (250, 100, 0))
        screen.blit(text, (30, 550))

    pygame.display.flip()
    clock.tick(tick_per_second)
pygame.quit()
