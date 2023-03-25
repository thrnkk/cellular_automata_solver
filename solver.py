from map import Map, Cell, Rule
from player import Player, PlayerDirection
import copy
import time
import sys

class MazeSolver(object):
    def __init__(self) -> None:
        self.result = []
        self.steps = 0
    
    def solve(self, map: Map, path: list[PlayerDirection] = []):
        self.steps += 1
        
        already_steped = False
        print(self.steps, len(path), map.player_position)
        
        new_map = copy.deepcopy(map)
        path_so_far = copy.deepcopy(path)
        
        if new_map.player_position['x'] == new_map.objective_position['x'] and new_map.player_position['y'] == new_map.objective_position['y']:
            self.result = path_so_far
            print('foi aqui')
            return True
        
        player = Player(new_map)
        directions = player.best_directions()
        
        if not directions:
            print('false: nulo')
            return False
        
        for (direction, distance) in directions:
            new_map = copy.deepcopy(map)
            player = Player(new_map)
            player.move(direction)
            
            new_map.step()
            
            print(f'append: {direction}')
            path_so_far.append(direction)
            
            if self.solve(new_map, path_so_far):
                return True
            
            print(f'pop: {direction}')
            path_so_far.pop()
        
        print('false')
        return False