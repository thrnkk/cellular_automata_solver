from map import Map, Cell
from enum import Enum
import copy
    
class PlayerDirection(Enum):
    UP = 1
    DOWN = 2
    RIGHT = 3
    LEFT = 4

class Player(object):
    def __init__(self, map: Map) -> None:
        self.map_object = map
        
    def set_map(self, map: Map):
        self.map_object = map
        
    def manhattan_distance(self, point1, point2) -> int:
        return sum(abs(value1 - value2) for value1, value2 in zip(point1, point2))

    def best_directions(self) -> tuple[PlayerDirection, int]:
        directions: dict = {}
        
        next_map = self.map_object.next_step(self.map_object.map)
        objective_point = (self.map_object.objective_position['x'], self.map_object.objective_position['y'])
        
        if (self.map_object.player_position['y'] > 0):
            x = self.map_object.player_position['x']
            y = self.map_object.player_position['y'] - 1
            
            if not next_map[y][x].alive:
                distance = self.manhattan_distance((x, y), objective_point)
                directions[PlayerDirection.UP] = distance

        if (self.map_object.player_position['y'] < len(self.map_object.map) - 1):
            x = self.map_object.player_position['x']
            y = self.map_object.player_position['y'] + 1
            
            if not next_map[y][x].alive:
                distance = self.manhattan_distance((x, y), objective_point)
                directions[PlayerDirection.DOWN] = distance
            
        if (self.map_object.player_position['x'] > 0):
            x = self.map_object.player_position['x'] - 1
            y = self.map_object.player_position['y']
            
            if not next_map[y][x].alive:
                distance = self.manhattan_distance((x, y), objective_point)
                directions[PlayerDirection.LEFT] = distance
            
        if (self.map_object.player_position['x'] < len(self.map_object.map[0]) - 1):
            x = self.map_object.player_position['x'] + 1
            y = self.map_object.player_position['y']
            
            if not next_map[y][x].alive:
                distance = self.manhattan_distance((x, y), objective_point)
                directions[PlayerDirection.RIGHT] = distance
                        
        best_directions = [direction for direction in sorted(directions.items(), key=lambda dir: dir[1])]
        
        return best_directions
        
    def move(self, direction: PlayerDirection):
        old_x = self.map_object.player_position['x']
        old_y = self.map_object.player_position['y']
        
        if direction == PlayerDirection.UP:
            self.map_object.player_position = {'x': old_x, 'y': old_y - 1}
            self.map_object.map[old_y][old_x].value = 0
            self.map_object.map[old_y - 1][old_x].value = 3
            
        if direction == PlayerDirection.DOWN:
            self.map_object.player_position = {'x': old_x, 'y': old_y + 1}
            self.map_object.map[old_y][old_x].value = 0
            self.map_object.map[old_y + 1][old_x].value = 3
            
        if direction == PlayerDirection.RIGHT:
            self.map_object.player_position = {'x': old_x + 1, 'y': old_y}
            self.map_object.map[old_y][old_x].value = 0
            self.map_object.map[old_y][old_x + 1].value = 3
            
        if direction == PlayerDirection.LEFT:
            self.map_object.player_position = {'x': old_x - 1, 'y': old_y}
            self.map_object.map[old_y][old_x].value = 0
            self.map_object.map[old_y][old_x - 1].value = 3
