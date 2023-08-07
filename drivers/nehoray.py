"""
This driver named Nehoray. This is the best driver in the whole ROSE universe!
"""
from rose.common import obstacles, actions  # NOQA

driver_name = "Nehoray"

bad_obstacles_side = [obstacles.BARRIER, obstacles.BIKE, obstacles.TRASH, obstacles.WATER, obstacles.CRACK]
bad_obstacles_forward = [obstacles.BARRIER, obstacles.BIKE, obstacles.TRASH]
actions_for_obs = {
    obstacles.PENGUIN: actions.PICKUP,
    obstacles.CRACK: actions.JUMP,
    obstacles.WATER: actions.BRAKE,
    obstacles.NONE: actions.NONE
}
scores = {
    actions.PICKUP: 10,
    actions.BRAKE: 4,
    actions.JUMP: 5,
    actions.RIGHT: 0,
    actions.LEFT: 0,
    actions.NONE: 0
}


def max_points():
    pass


def best_direction(matrix):
    if matrix[0][1] not in bad_obstacles_forward:
        return actions_for_obs[matrix[0][1]]
        # if matrix[0][1] == obstacles.PENGUIN:
        #     return actions.PICKUP
        # if matrix[0][1] == obstacles.CRACK:
        #     return actions.JUMP
        # if matrix[0][1] == obstacles.WATER:
        #     return actions.BRAKE
        # if matrix[0][1] == obstacles.NONE:
        #     return actions.NONE
    if matrix[0][2] not in bad_obstacles_side and matrix[0][2] is not None:
        return actions.RIGHT
    else:
        return actions.LEFT


def drive(world):
    x = world.car.x
    y = world.car.y
    direction_matrix = []
    try:
        direction_matrix = [
            [world.get((x - 1, y - 1)), world.get((x, y - 1)), world.get((x + 1, y - 1))],
            [world.get((x - 1, y - 2)), world.get((x, y - 2)), world.get((x + 1, y - 2))],
            [world.get((x - 1, y - 3)), world.get((x, y - 3)), world.get((x + 1, y - 3))],
            [world.get((x - 1, y - 4)), world.get((x, y - 4)), world.get((x + 1, y - 4))],
            [world.get((x - 1, y - 5)), world.get((x, y - 5)), world.get((x + 1, y - 5))],
            [world.get((x - 1, y - 6)), world.get((x, y - 6)), world.get((x + 1, y - 6))]
        ]
    except IndexError:
        if x - 1 < 0:
            direction_matrix = [
                [None, world.get((x, y - 1)), world.get((x + 1, y - 1))],
                [None, world.get((x, y - 2)), world.get((x + 1, y - 2))],
                [None, world.get((x, y - 3)), world.get((x + 1, y - 3))],
                [None, world.get((x, y - 4)), world.get((x + 1, y - 4))],
                [None, world.get((x, y - 5)), world.get((x + 1, y - 5))],
                [None, world.get((x, y - 6)), world.get((x + 1, y - 6))]
            ]
        else:
            direction_matrix = [
                [world.get((x - 1, y - 1)), world.get((x, y - 1)), None],
                [world.get((x - 1, y - 2)), world.get((x, y - 2)), None],
                [world.get((x - 1, y - 3)), world.get((x, y - 3)), None],
                [world.get((x - 1, y - 4)), world.get((x, y - 4)), None],
                [world.get((x - 1, y - 5)), world.get((x, y - 5)), None],
                [world.get((x - 1, y - 6)), world.get((x, y - 6)), None]
            ]
    return best_direction(direction_matrix)
