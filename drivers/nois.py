from rose.common import obstacles, actions
"""
Fr Fr the best driver in the whole ROSE planet!
"""
driver_name = "N.O.I.S"  # N.O.I.S - Nehoray, Or, Itzhak, Shani


def encounter_obstacle_forward(x, y, world):
    """
    param: x - x cord of the car
    param: y - y cord of the car
    param: world - world object to work with
    This function resolves and gives us the best solution to pass by forward obstacles without losing points!
    """
    if x == 0 or x == 3:  # Check out of range right
        return actions.RIGHT
    elif x == 2 or x == 5:  # Check out of range left
        return actions.LEFT
    if world.get((x+1, y-2)) == obstacles.PENGUIN:
        return actions.RIGHT
    elif world.get((x-1, y-2)) == obstacles.PENGUIN:
        return actions.LEFT
    elif world.get((x+1, y-2)) == obstacles.CRACK:
        return actions.RIGHT
    elif world.get((x-1, y-2)) == obstacles.CRACK:
        return actions.LEFT
    elif world.get((x+1, y-2)) == obstacles.WATER:
        return actions.RIGHT
    elif world.get((x-1, y-2)) == obstacles.WATER:
        return actions.LEFT
    else:
        return actions.LEFT


def no_obstacle_forward(x, y, world):
    """
    param: x - x cord of the car
    param: y - y cord of the car
    param: world - world object to work with
    This function maximize the points by analyzing two steps forward to know which direction is the best for us.
    """
    if x == 0 or x == 3:  # Check out of range right
        if world.get((x+1, y-2)) in (obstacles.PENGUIN, obstacles.WATER, obstacles.CRACK):
            return actions.RIGHT
        else:
            return actions.NONE
    elif x == 2 or x == 5:  # Check out of range left
        if world.get((x-1, y-2)) in (obstacles.PENGUIN, obstacles.WATER, obstacles.CRACK):
            return actions.LEFT
        else:
            return actions.NONE
    else:
        if world.get((x+1, y-2)) == obstacles.PENGUIN:
            return actions.RIGHT
        elif world.get((x-1, y-2)) == obstacles.PENGUIN:
            return actions.LEFT
        elif world.get((x+1, y-2)) == obstacles.CRACK:
            return actions.RIGHT
        elif world.get((x-1, y-2)) == obstacles.CRACK:
            return actions.LEFT
        elif world.get((x+1, y-2)) == obstacles.WATER:
            return actions.RIGHT
        elif world.get((x-1, y-2)) == obstacles.WATER:
            return actions.LEFT
        else:
            return actions.NONE


def drive(world):
    x = world.car.x
    y = world.car.y
    if world.get((x, y-1)) == obstacles.PENGUIN:
        return actions.PICKUP
    elif world.get((x, y-1)) == obstacles.WATER:
        return actions.BRAKE
    elif world.get((x, y-1)) == obstacles.CRACK:
        return actions.JUMP
    elif world.get((x, y-1)) in (obstacles.TRASH, obstacles.BIKE, obstacles.BARRIER):
        return encounter_obstacle_forward(x, y, world)
    elif world.get((x, y-1)) == obstacles.NONE:
        return no_obstacle_forward(x, y, world)
    else:
        return actions.NONE
