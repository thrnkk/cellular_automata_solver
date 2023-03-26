from map import Map, Cell, Rule
from player import Player, PlayerDirection
import copy
import time
import sys

class MazeSolver(object):
    def __init__(self) -> None:
        self.result = []
        self.seconds = 0
        self.steps = 0
        
    def solve(self, map: Map):
        start = time.time()
        self._solve(map, [])
        end = time.time()
        self.seconds = round(end - start, 2)
    
    def _solve(self, map: Map, path: list[PlayerDirection] = []):
        self.steps += 1
        
        new_map = copy.deepcopy(map)
        path_so_far = copy.deepcopy(path)
        
        if new_map.player_position['x'] == new_map.objective_position['x'] and new_map.player_position['y'] == new_map.objective_position['y']:
            self.result = path_so_far
            return True
        
        player = Player(new_map)
        directions = player.best_directions()
        
        for direction, distance in directions:
            new_map = copy.deepcopy(map)
            player = Player(new_map)
            player.move(direction)
            
            new_map.step()
            path_so_far.append(direction)
            
            if self._solve(new_map, path_so_far):
                return True
            
            path_so_far.pop()

        return False
    
    def pretty_print(self):
        
        if len(self.result) > 0:
            print(" ".join(list(map(lambda x: x.value, self.result))))