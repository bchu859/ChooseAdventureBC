import pygame
import sys
import os
import random
import math
import time

os.environ['SDL_VIDEO_CENTERED'] = '1'

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 205, 0)
PURPLE = (150, 50, 200)
YELLOW = (255, 245, 50)
RED = (255, 0, 0)
BLUE = (50, 135, 255)
fps = 30
loop_counter = 0
winner = "winner"
SHIP_WIDTH = SHIP_HEIGHT = 13
PILL_WIDTH = 7
PILL_HEIGHT = 25
size = WIDTH, HEIGHT = 920, 570
lwin_count = 0
rwin_count = 0
timer = 0
pygame.init()


class Game:
    def __init__(self):
        self.density = SHIP_WIDTH * SHIP_HEIGHT
        self.screen = pygame.display.set_mode(size, pygame.SRCALPHA)
        self.clock = pygame.time.Clock()
        self.play = self.intro = True
        self.outro = False
        self.vertical = pygame.Surface((1, HEIGHT)).convert()
        self.horizontal = pygame.Surface((WIDTH, 1))
        self.intro_back = self.screen
        self.intro_back = pygame.transform.scale(self.intro_back, (WIDTH, HEIGHT))
        self.intro_rect = self.intro_back.get_rect()
        self.outro_back = self.screen
        self.outro_back = pygame.transform.scale(self.outro_back, (WIDTH, HEIGHT))
        self.outro_rect = self.outro_back.get_rect()

        self.left_wins = Text(50, 'Wins:' + str(lwin_count), WIDTH / 3, HEIGHT/50, BLACK)
        self.right_wins = Text(50, 'Wins:' + str(rwin_count), WIDTH/1.3, HEIGHT / 50, BLACK)
        self.title = Text(120, 'Density', WIDTH/3.2, HEIGHT/4, WHITE)
        self.subtitle = Text(90, '-- Click Here --', WIDTH / 4, HEIGHT/1.8, WHITE)
        self.endtitle = Text(120, winner + 'Player Wins!!!', WIDTH/10, HEIGHT/4, WHITE)
        self.left_density = Text(50, 'Density:' + str(self.density), WIDTH / 15, HEIGHT/50, BLACK)
        self.right_density = Text(50, "Density:" + str(self.density), WIDTH / 2.01, HEIGHT/50, BLACK)

    def blink(self, subtitle, subtitle_rect):
        if pygame.time.get_ticks() % 1000 < 500:
            self.screen.blit(subtitle, subtitle_rect)

    def restart(self, lship, rship):
        lship.rect.width = lship.rect.height = 13
        rship.rect.width = rship.rect.height = 13
        lship.rect.x = WIDTH / 4 - SHIP_WIDTH/2

        lship.rect.y = HEIGHT - (4 * SHIP_HEIGHT)
        rship.rect.x = (WIDTH * 3) / 4 - SHIP_WIDTH / 2
        rship.rect.y = HEIGHT - (4 * SHIP_HEIGHT)
        lship.density = 169
        rship.density = 169
        time.sleep(1.5)

    def update(self, lship, rship, ship_group):
        global lwin_count, rwin_count, winner
        self.left_density.image = self.left_density.font.render('Density:' + str(lship.density - 169), 1, BLACK)
        self.right_density.image = self.right_density.font.render('Density:' + str(rship.density - 169), 1, BLACK)

        if lship.density - 169 >= 3000:
            lship.density += 500
            lship.rect.x -= math.sqrt(.005)
            lship.rect.y -= math.sqrt(.005)

            if rship.density > 20:
                rship.density -= 20

            else:
                rship.kill()

        elif rship.density - 169 >= 3000:
            rship.density += 500
            rship.rect.x -= math.sqrt(.005)
            rship.rect.y -= math.sqrt(.005)

            if lship.density > 20:
                lship.density -= 20
            else:
                lship.kill()

        if lship.density - 169 >= 100000:
            lwin_count += 1
            self.restart(lship, rship)
            ship_group.add(rship)

        elif rship.density - 169 >= 100000:
            rwin_count += 1
            self.restart(lship, rship)
            ship_group.add(lship)

        if lwin_count >= 3:
            winner = "Left"
            lwin_count = rwin_count = 0

            self.play = False
            self.outro = True

        elif rwin_count >= 3:
            winner = "Right"
            rwin_count = lwin_count = 0
            self.play = False
            self.outro = True

        self.left_wins.image = self.left_wins.font.render('Wins:' + str(lwin_count), 1, BLACK)
        self.right_wins.image = self.right_wins.font.render('Wins:' + str(rwin_count), 1, BLACK)
        self.endtitle.image = self.endtitle.font.render(winner + ' Player Wins!!!', 1, WHITE)


class Text:
    def __init__(self, size, text, xpos, ypos, color):
        self.font = pygame.font.SysFont('Britannic Bold', size)
        self.image = self.font.render(text, 1, color)
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(xpos, ypos)


class Ship(pygame.sprite.Sprite):
    def __init__(self, x, y, side):
        pygame.sprite.Sprite.__init__(self)
        self.win = False
        self.speed = 5
        self.density = SHIP_WIDTH * SHIP_HEIGHT
        self.type = side
        self.image = pygame.Surface((math.sqrt(self.density), math.sqrt(self.density))).convert()
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(x, y)


    def move_ship(self):
        key = pygame.key.get_pressed()
        # Left Ship movement
        if self.type == "left":
            if key[pygame.K_w]:
                self.rect.y -= self.speed
            if key[pygame.K_s]:
                self.rect.y += self.speed
            if key[pygame.K_d]:
                self.rect.x += self.speed
            if key[pygame.K_a]:
                self.rect.x -= self.speed
         # Right Ship movement
        elif self.type == "right":
            if key[pygame.K_UP]:
                self.rect.y -= self.speed
            if key[pygame.K_DOWN]:
                self.rect.y += self.speed
            if key[pygame.K_RIGHT]:
                self.rect.x += self.speed
            if key[pygame.K_LEFT]:
                self.rect.x -= self.speed

    def move_inbound(self):
        # Left Ship Boundaries
        if self.type == "left":
            if self.rect.right > WIDTH / 2:
                self.rect.right = WIDTH / 2
            if self.rect.top < 50:
                self.rect.top = 50
            if self.rect.bottom > 570:
                self.rect.bottom = 570
            if self.rect.left < 0:
                self.rect.right = WIDTH / 2
        # Right Ship Boundaries
        elif self.type == "right":
            if self.rect.left < WIDTH / 2:
                self.rect.left = WIDTH / 2
            if self.rect.top < 50:
                self.rect.top = 50
            if self.rect.bottom > 570:
                self.rect.bottom = 570
            if self.rect.right > 920:
                self.rect.left = WIDTH / 2

    def update(self, pill_group, powerup_group, ship_group):
        # Ship movement
        self.move_ship()
        self.move_inbound()

        collisions = pygame.sprite.spritecollide(self, pill_group, True)
        for p in collisions:
            self.density += p.density * 50

        self.rect.width = self.rect.height = math.sqrt(self.density)
        self.image = pygame.transform.scale(self.image, (self.rect.width, self.rect.height))

        collisions = pygame.sprite.spritecollide(self, powerup_group, True)
        for p in collisions:
            if p.type == 1:
                for s in ship_group:
                    if self.type != s.type:
                        s.speed = 2
            elif p.type == 2:
                self.speed = 15
            elif p.type == 3:
                self.density += 500

class Pill(pygame.sprite.Sprite):
    def __init__(self, x, density):
        pygame.sprite.Sprite.__init__(self)
        self.speed = 3
        self.density = density
        self.image = pygame.Surface((PILL_WIDTH, PILL_HEIGHT)).convert()
        self.image.fill(self.set_color())
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(x, HEIGHT/15)

    def set_color(self):
        if self.density == 1:
            return YELLOW
        elif self.density == 2:
            return GREEN
        elif self.density == 3:
            return RED
        elif self.density == 4:
            return BLUE

    def update(self):
        self.rect = self.rect.move((0, self.speed))
        if self.rect.y > HEIGHT:
            self.kill()


class Powerups(pygame.sprite.Sprite):
    # powerups = slow down, speed up, money
    def __init__(self, type):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10, 10)).convert()
        self.rect = self.image.get_rect()
        self.type = type
        self.color = (244, 142, 168)
        self.rect.x = random.randrange(0, 1000)
        self.rect.y = random.randrange(0, 1000)
        self.start = pygame.time.get_ticks()

    def slow_down(self, pill_group, powerup_group, ship_group):
        global timer
        effect = True
        for ship in ship_group:
            if effect:
                ship.update(pill_group, powerup_group, ship_group)
                if pygame.time.get_ticks() - self.start >= 10:
                    effect = False

    def speed_up(self, pill_group, powerup_group, ship_group):
        global timer
        effect = True
        for ship in ship_group:
            if effect:
                ship.update(pill_group, powerup_group, ship_group)
                if pygame.time.get_ticks() - self.start >= 10:
                    effect = False

    def money(self, pill_group, powerup_group, ship_group):
        effect = True
        for ship in ship_group:
            if effect:
                ship.update(pill_group, powerup_group, ship_group)
                if pygame.time.get_ticks() - self.start >= 10:
                    effect = False


def main():
    global fps, loop_counter, WIDTH, HEIGHT, timer
    pygame.display.set_caption('Density')
    run = Game()

    ship_l = Ship(WIDTH/4 - SHIP_WIDTH/2, HEIGHT - (4 * SHIP_HEIGHT), "left")
    ship_r = Ship((WIDTH * 3) / 4 - SHIP_WIDTH/2, HEIGHT - (4 * SHIP_HEIGHT), "right")

    ship_group = pygame.sprite.Group()
    ship_group.add(ship_l, ship_r)
    pill_group = pygame.sprite.Group()
    powerup_group = pygame.sprite.Group()

    while run.intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN or pygame.key.get_pressed()[pygame.K_RETURN] != 0:
                run.intro = False

        run.screen.blit(run.intro_back, run.intro_rect)
        run.screen.blit(run.title.image, run.title.rect)
        run.blink(run.subtitle.image, run.subtitle.rect)
        run.clock.tick(fps)
        pygame.display.flip()

    while True:
        while run.play:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.QUIT()
                        sys.exit()

            ship_group.update(pill_group, powerup_group, ship_group)
            pill_group.update()
            run.update(ship_l, ship_r, ship_group)

            if loop_counter % 10 == 0:
                pill = Pill(random.randrange(0, (WIDTH/2) - PILL_WIDTH), int(random.choice('1111111111111111122222233344')))
                pill2 = Pill(random.randrange(WIDTH/2, (WIDTH - PILL_WIDTH)), int(random.choice('1111111111111111122222233344')))
                pill_group.add(pill, pill2)

            if loop_counter % 100 == 0:
                powerup = Powerups(int(random.choice('123')))
                if powerup.type == 1:
                    powerup.slow_down(pill_group, powerup_group, ship_group)
                    powerup_group.add(powerup)
                elif powerup.type == 2:
                    powerup.speed_up(pill_group, powerup_group, ship_group)
                    powerup_group.add(powerup)
                elif powerup.type == 3:
                    powerup.money(ship_group, pill_group, powerup_group)
                    powerup_group.add(powerup)

            run.screen.fill(WHITE)
            ship_group.draw(run.screen)
            pill_group.draw(run.screen)
            powerup_group.draw(run.screen)
            run.screen.blit(run.vertical, (WIDTH/2, HEIGHT/15))
            run.screen.blit(run.horizontal, (0, HEIGHT/15))
            run.screen.blit(run.left_density.image, run.left_density.rect)
            run.screen.blit(run.right_density.image, run.right_density.rect)
            run.screen.blit(run.left_wins.image, run.left_wins.rect)
            run.screen.blit(run.right_wins.image, run.right_wins.rect)
            loop_counter += 1
            timer += 1
            run.clock.tick(fps)
            pygame.display.flip()

            while run.outro:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT: sys.exit()
                    if event.type == pygame.MOUSEBUTTONDOWN or pygame.key.get_pressed()[pygame.K_RETURN] != 0:

                        run.outro = False
                        run.play = True

                run.screen.blit(run.outro_back, run.outro_rect)
                run.screen.blit(run.endtitle.image, run.endtitle.rect)
                run.blink(run.subtitle.image, run.subtitle.rect)
                run.clock.tick(fps)
                pygame.display.flip()


if __name__ == "__main__":
    main()
