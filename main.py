import pygame as pg
import sys
from settings import *
from map import *
from player import *
from raycasting import *
from object_renderer import *
from sprite_object import *
from object_handler import *
from weapon import *
from sound import *
from pathfinding import *


class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode(RES)
        pg.mouse.set_visible(False)
        self.clock = pg.time.Clock()
        self.delta_time = 1
        self.global_trigger = False
        self.global_event = pg.USEREVENT + 0
        self.gameStarted = False
        self.condition = False
        self.score = 0
        pg.time.set_timer(self.global_event, 40)
        pg.display.set_caption('Scouts-Many-Marshes')

    def mainMenu(self):
        self.UI_menu()
        if self.gameStarted == False:
            for event in pg.event.get():
                if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                    pg.quit()
                elif event.type == pg.MOUSEBUTTONDOWN:
                    self.gameStarted = True
                    self.load_level('forest')

    def UI_menu(self):
        pg.display.flip()
        pg.draw.rect(self.screen, (0, 30, 30), (0, 0, WIDTH, HEIGHT))
        self.main_menu = pg.image.load('resources/sprites/static_sprites/main_menu_text.png').convert_alpha()
        self.font = pg.font.Font('resources/textures/GorgeousPixel.ttf', 70)
        self.mainMenuText = self.font.render('scouts many marshes', True, 'darkgreen')
        self.screen.blit(self.mainMenuText, (28, 12))
        self.mainMenuText = self.font.render('scouts many marshes', True, 'green')
        self.screen.blit(self.mainMenuText, (22, 7))
        self.font = pg.font.Font('resources/textures/GorgeousPixel.ttf', 30)
        self.mainMenuText = self.font.render('press any Mouse Button to start', True, 'white')
        self.screen.blit(self.mainMenuText, (0, HEIGHT - 30))
        self.screen.blit(self.main_menu, (HALF_WIDTH - 150, HALF_HEIGHT - 250))

    def load_level(self, lvl_type):
        pg.display.flip()
        self.map = Map(self, lvl_type)
        self.player = Player(self)
        self.object_renderer = ObjectRenderer(self)
        self.raycasting = RayCasting(self)
        self.object_handler = ObjectHandler(self)
        self.weapon = Weapon(self)
        self.sound = Sound(self)
        self.pathfinding = PathFinding(self)
        pg.mixer.music.play(-1)

    def update(self):
        self.player.update()
        self.raycasting.update()
        self.object_handler.update()
        self.weapon.update()
        pg.display.flip()
        self.delta_time = self.clock.tick(FPS)
        self.score += 0.01

    def draw(self):
        self.object_renderer.draw()
        self.weapon.draw()

    def check_events(self):
        self.global_trigger = False
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()
            elif event.type == self.global_event:
                self.global_trigger = True
            elif self.condition:
                if event.type == pg.KEYDOWN and event.key == pg.K_e:
                    self.new_level()
                if event.type == pg.KEYDOWN and event.key == pg.K_c:
                    print(self.player.map_pos())
            self.player.single_fire_event(event)

    def new_level(self):
        pg.display.flip()
        self.load_level('dungeon')
        self.sound.where.play()
        self.condition = False

    def run(self):
        while True:
            if not self.gameStarted:
                self.mainMenu()
            elif self.gameStarted:
                self.check_events()
                self.update()
                self.draw()


if __name__ == '__main__':
    game = Game()
    game.run()
