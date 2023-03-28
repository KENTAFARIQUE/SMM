import pygame as pg

class Sound:
    def __init__(self, game):
        self.game = game
        pg.mixer.init()
        self.path = 'resources/sound/'
        self.knife = pg.mixer.Sound(self.path + 'swoosh.wav')
        self.npc_pain = pg.mixer.Sound(self.path + 'npc_pain.wav')
        self.npc_death = pg.mixer.Sound(self.path + 'npc_death.wav')
        self.npc_shot = pg.mixer.Sound(self.path + 'npc_attack.wav')
        self.pudge = pg.mixer.Sound(self.path + 'pudge.mpeg')
        self.npc_shot.set_volume(0.1)
        self.npc_pain.set_volume(0.2)
        self.npc_death.set_volume(0.2)
        self.knife.set_volume(0.2)
        self.player_pain = pg.mixer.Sound(self.path + 'player_pain.wav')
        self.where = pg.mixer.Sound(self.path + 'where.mp3')
        if self.game.map.level == 'forest':
            self.ambient = pg.mixer.music.load(self.path + 'ambient.wav')
        else:
            self.ambient = pg.mixer.music.load(self.path + 'secret.mp3')
        pg.mixer.music.set_volume(0.1)
