"""
This driver named Itzhack. This is the best driver in whole ROSE universe!
"""
from rose.common import obstacles, actions  # NOQA

driver_name = "Itzhack"
bad_ops_side = [obstacles.BARRIER,obstacles.TRASH,obstacles.BIKE]
act_ops = [obstacles.WATER,obstacles.PENGUIN,obstacles.CRACK]
# points for each action:
act = {actions.PICKUP : 10,
       actions.JUMP : 5,
       actions.BRAKE : 4}
try:
    matrix = [[world.get((x-1,y-3)),world.get((x,y-3)),world.get((x+1,y-3))],
              [world.get((x-1,y-2)),world.get((x,y-2)),world.get((x+1,y-2))],
              [world.get((x-1,y-1)),world.get((x,y-1)),world.get((x+1,y-1))]]
except indexError:
    if x-1 < 0:
        matrix = [[None, world.get((x, y - 3)), world.get((x + 1, y - 3))],
                  [None, world.get((x, y - 2)), world.get((x + 1, y - 2))],
                  [None, world.get((x, y - 1)), world.get((x + 1, y - 1))]]
    else:
        matrix = [[world.get((x - 1, y - 3)), world.get((x, y - 3)), None],
                  [world.get((x - 1, y - 2)), world.get((x, y - 2)), None],
                  [world.get((x - 1, y - 1)), world.get((x, y - 1)), None]]


def route_points(matrix):
    route_p = [0,0,0]
    for y in range(3):
        sum = 0
        for x in range(3):
            if matrix[x][y] == obstacles.PENGUIN:
                sum+=10
            elif matrix[x][y] == obstacles.CRACK:
                sum += 5
            elif matrix[x][y] == obstacles.WATER:
                sum += 4
        route_p[y] = sum
    return route_p

def is_max(arr):
    if arr[0] > arr[1] and arr[0] > arr [2]:
        return 0
    elif arr[1] > arr[0] and arr[1] > arr [2]:
        return 1
    return 2


def go_best_route(matrix ,route_p):
    if is_max(route_p) == 0 and matrix[1][0] is not None:
        if matrix[1][0] not in bad_ops_side:
            return actions.LEFT
        else:
            if is_max([route_p[1],route_p[2]]) == 2 and matrix[1][2] is not None:
                if matrix[1][2] not in bad_ops_side:
                    return actions.RIGHT
    return actions.NONE










# Choose the best action for obstacle

