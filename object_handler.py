from sprite_object import *
from npc import *
from random import choices, randrange, uniform


class ObjectHandler:
    def __init__(self, game):
        self.game = game
        self.sprite_list = []
        self.npc_list = []
        self.npc_sprite_path = 'resources/sprites/npc/'
        self.static_sprite_path = 'resources/sprites/static_sprites/'
        self.anim_sprite_path = 'resources/sprites/artefact/'
        add_sprite = self.add_sprite
        add_npc = self.add_npc
        self.npc_positions = {}
        self.artifact_pos = (36, 18)

        # spawn npc
        if self.game.map.level == 'forest':
            self.enemies = 7
        if self.game.map.level == 'dungeon':
            self.enemies = 3
        self.npc_types = [GhostNPC, FaceNPC]
        if self.game.map.level == 'forest':
            self.weights = [100, 0]
        else:
            self.weights = [0, 100]
        self.restricted_area = {(i, j) for i in range(10) for j in range(10)}
        self.spawn_npc()

        # sprite map
        if game.map.level == 'forest':
            s = -0.35
            for i in range(1000):
                add_sprite(SpriteObject(game, pos=(randrange(-100, 100), randrange(-100, 100)), scale=3, shift=s,
                                        path='resources/sprites/static_sprites/tree2.png'))
                add_sprite(SpriteObject(game, pos=(randrange(-100, 100), randrange(-100, 100)), scale=3, shift=s,
                                        path='resources/sprites/static_sprites/tree1.png'))
                add_sprite(SpriteObject(game, pos=(randrange(-100, 100), randrange(-100, 100)), scale=uniform(0.6, 0.7),
                                        shift=uniform(0.3, 0.4),
                                        path='resources/sprites/static_sprites/bush.png'))
        else:
            add_sprite(AnimatedSprite(game, path=self.anim_sprite_path + '0.png', pos=self.artifact_pos))

    def spawn_npc(self):
        for i in range(self.enemies):
            npc = choices(self.npc_types, self.weights)[0]
            pos = x, y = randrange(self.game.map.cols), randrange(self.game.map.rows)
            while (pos in self.game.map.world_map) or (pos in self.restricted_area):
                pos = x, y = randrange(self.game.map.cols), randrange(self.game.map.rows)
            self.add_npc(npc(self.game, pos=(x + 0.5, y + 0.5)))

    def check_win(self):
        pass

    def update(self):
        self.npc_positions = {npc.map_pos for npc in self.npc_list if npc.alive}
        [sprite.update() for sprite in self.sprite_list]
        [npc.update() for npc in self.npc_list]
        self.check_win()

    def add_npc(self, npc):
        self.npc_list.append(npc)

    def add_sprite(self, sprite):
        self.sprite_list.append(sprite)
