import pygame as pg
from settings import *
from player import *


class ObjectRenderer:
    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.wall_textures = self.load_wall_textures()
        self.sky_image = self.get_texture('resources/textures/sky.png', (WIDTH, HALF_HEIGHT))
        self.sky_offset = 0
        self.blood_screen = self.get_texture('resources/textures/blood_screen.png', RES)
        self.hp_bar = self.get_texture('resources/textures/UI.png', (150, 100))
        self.font1 = pg.font.Font('resources/textures/GorgeousPixel.ttf', 40)
        self.font2 = pg.font.Font('resources/textures/GorgeousPixel.ttf', 20)
        self.font3 = pg.font.Font('resources/textures/GorgeousPixel.ttf', 60)
        self.die_text = self.font1.render('YOU DIED', True, 'darkred')
        self.win_text = self.font3.render(f'score:{int(self.game.score)}', True, 'green')
        self.text1 = self.font2.render('press "e" to go to the dungeon', True, 'white')

    def draw(self):
        self.draw_background()
        self.render_game_objects()
        self.draw_player_health()
        self.draw_enemy_counter()
        self.draw_crosshair()

    def win(self):
        pg.draw.rect(self.screen, 'black', (0, 0, WIDTH, HEIGHT))
        self.screen.blit(self.win_text, (HALF_WIDTH - 150, HALF_HEIGHT + 30))

    def game_over(self):
        pg.draw.rect(self.screen, 'black', (0, 0, WIDTH, HEIGHT))
        self.screen.blit(self.die_text, (HALF_WIDTH - 150, HALF_HEIGHT + 30))

    def draw_player_health(self):
        self.HP_text = self.font1.render(str(self.game.player.health) + '%', True, 'darkred')
        self.screen.blit(self.hp_bar, (0, HEIGHT - 100))
        self.screen.blit(self.HP_text, (50, HEIGHT - 75))

    def draw_enemy_counter(self):
        if self.game.map.level == 'forest':
            self.enemies = self.font2.render(
                f'killed {self.game.player.enemy_kills} (remain: {GOAL - self.game.player.enemy_kills})', True, 'white')
            self.screen.blit(self.enemies, (0, 0))
            if self.game.player.enemy_kills == GOAL:
                self.screen.blit(self.text1, (HALF_WIDTH - 155, HALF_HEIGHT + 20))
        else:
            self.enemies = self.font2.render(
                'you need to find the artifact', True, 'white')
            self.screen.blit(self.enemies, (0, 0))

    def draw_crosshair(self):
        pg.draw.rect(self.screen, 'white', (HALF_WIDTH - 1, HALF_HEIGHT - 1, 3, 3))

    def player_damage(self):
        self.screen.blit(self.blood_screen, (0, 0))

    def draw_background(self):
        if self.game.map.level == 'forest':
            self.sky_offset = (self.sky_offset + 4.5 * self.game.player.rel) % WIDTH
            self.screen.blit(self.sky_image, (-self.sky_offset, 0))
            self.screen.blit(self.sky_image, (-self.sky_offset + WIDTH, 0))

            pg.draw.rect(self.screen, FLOOR_COLOR1, (0, HALF_HEIGHT, WIDTH, HEIGHT))
        else:
            pg.draw.rect(self.screen, CEILING_COLOR, (0, 0, WIDTH, HEIGHT))
            pg.draw.rect(self.screen, FLOOR_COLOR2, (0, HALF_HEIGHT, WIDTH, HEIGHT))

    def render_game_objects(self):
        list_objects = sorted(self.game.raycasting.objects_to_render, key=lambda t: t[0], reverse=True)
        for depth, image, pos in list_objects:
            self.screen.blit(image, pos)

    @staticmethod
    def get_texture(path, res=(TEXTURE_SIZE, TEXTURE_SIZE)):
        texture = pg.image.load(path).convert_alpha()
        return pg.transform.scale(texture, res)

    def load_wall_textures(self):
        return {
            1: self.get_texture('resources/textures/1.png'),
            2: self.get_texture('resources/textures/2.png'),
            3: self.get_texture('resources/textures/3.png'),
        }
