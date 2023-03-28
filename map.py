import pygame as pg
import csv


forest_map = []
with open('resources/forest_map.csv', encoding="utf8") as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for index, row in enumerate(reader):
        for j in range(len(row)):
            row[j] = int(row[j])
        forest_map.append(row)

dungeon_map = []
with open('resources/dungeon_map.csv', encoding="utf8") as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for index, row in enumerate(reader):
        for j in range(len(row)):
            row[j] = int(row[j])
        dungeon_map.append(row)


class Map:
    def __init__(self, game, level):
        self.level = level
        self.game = game
        if level == 'forest':
            self.map = forest_map
        else:
            self.map = dungeon_map
        self.world_map = {}
        self.rows = len(self.map)
        self.cols = len(self.map[0])
        self.get_map()

    def get_map(self):
        for j, row in enumerate(self.map):
            for i, value in enumerate(row):
                if value:
                    self.world_map[(i, j)] = value
