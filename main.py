from map import Map, Rule
from player import Player
from solver import MazeSolver

if __name__ == '__main__':
    map_object = Map(Rule(3, 6), Rule(1, 5))
    map_object.set_map(map_object._import_file('./files/input.txt'))
    player_object = Player()
    maze_solver = MazeSolver()
    counter = 0

    maze_solver.solve(map_object)
    maze_solver.pretty_print()
    path = maze_solver.result
    print(f'São necessários: {len(path)} passos para resolver.')
    print(f'Foram checados {maze_solver.steps} passsos.')
    print(f'Foram necessários {maze_solver.seconds} segundos para resolver.')