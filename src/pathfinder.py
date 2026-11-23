from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder

def find_path_a_star(env, start_position: tuple, target_position: tuple):

    matrix = []
    for y in range(env.height):
        row = []
        for x in range(env.width):
            if env.is_free((x, y)):
                row.append(1)  # Walkable
            else:
                row.append(0)  # Obstacle
        matrix.append(row)

    grid = Grid(matrix=matrix)

    start_node = grid.node(start_position[0], start_position[1])
    end_node = grid.node(target_position[0], target_position[1])


    path, runs = AStarFinder().find_path(start_node, end_node, grid)

    coordinate_path = [(node.x, node.y) for node in path]
    
    return coordinate_path