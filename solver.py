from map import Map
from player import Player
import copy
import time
from collections import deque

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
    
    def _solve(self, map: Map, path: deque = deque()):
        self.steps += 1
        
        if map.player_position.x == map.objective_position.x and map.player_position.y == map.objective_position.y:
            self.result = path
            return True
        
        player = Player()
        directions = player.best_directions(map)
        
        for direction, distance in directions:
            new_map = copy.deepcopy(map)
            new_map.move_player(direction)
            
            new_map.step()
            path.append(direction)
            
            if self._solve(new_map, path):
                return True
            
            path.pop()

        return False
    
    def pretty_print(self):
        
        if len(self.result) > 0:
            print(" ".join(list(map(lambda x: x.value, self.result))))