""" Mystery Obstacle """

import random


ARMOR = "armor"
DOUBLE = "double"
CHANGE = "change"
CONFUSION = "confusion"

ALL = [CHANGE, CONFUSION]


def get_random_reward():
    return random.choice(ALL)


def activate_armor(player):
    player.has_armor = True
    player.armor_frames = 8
    print("Armor Activated")
