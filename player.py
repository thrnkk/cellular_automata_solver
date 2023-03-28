from map import Map
from utility import PlayerDirection

class Player(object):
    def __init__(self) -> None:
        pass
        
    def manhattan_distance(self, point1, point2) -> int:
        return sum(abs(value1 - value2) for value1, value2 in zip(point1, point2))

    def best_directions(self, map: Map) -> tuple[PlayerDirection, int]:
        directions: dict = {}
        
        next_map = map.next_step(map.map)
        objective_point = (map.objective_position.x, map.objective_position.y)
        
        if (map.player_position.y > 0):
            x = map.player_position.x
            y = map.player_position.y - 1
            
            if not next_map[y][x].alive:
                distance = self.manhattan_distance((x, y), objective_point)
                directions[PlayerDirection.UP] = distance

        if (map.player_position.y < len(map.map) - 1):
            x = map.player_position.x
            y = map.player_position.y + 1
            
            if not next_map[y][x].alive:
                distance = self.manhattan_distance((x, y), objective_point)
                directions[PlayerDirection.DOWN] = distance
            
        if (map.player_position.x > 0):
            x = map.player_position.x - 1
            y = map.player_position.y
            
            if not next_map[y][x].alive:
                distance = self.manhattan_distance((x, y), objective_point)
                directions[PlayerDirection.LEFT] = distance
            
        if (map.player_position.x < len(map.map[0]) - 1):
            x = map.player_position.x + 1
            y = map.player_position.y
            
            if not next_map[y][x].alive:
                distance = self.manhattan_distance((x, y), objective_point)
                directions[PlayerDirection.RIGHT] = distance
                        
        best_directions = [direction for direction in sorted(directions.items(), key=lambda dir: dir[1])]
        
        return best_directions