import copy
from utility import PlayerDirection

class Cell(object):
    def __init__(self, value: int = 0, alive: bool = False) -> None:
        self.value = value
        self.alive = alive
        
    def __str__(self):
        return f'{self.value}'

class Rule(object):
    def __init__(self, gt: int, lt: int) -> None:
        self.greater_than = gt
        self.lower_than = lt
    
    def __str__(self):
        return f'GT: {self.greater_than} | LT: {self.lower_than}'
    
class Point(object):
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y
        
class Map(object):
    def __init__(self, survivor_rule: Rule, birth_rule: Rule) -> None:
        self.survivor_rule = survivor_rule
        self.birth_rule = birth_rule
        
        self.objective_position = Point(0, 0)
        self.player_position = Point(0, 0)
        
        self.map = [[]]
        
    def set_map(self, map: list[list[Cell]]):
        self.map = map
        
    def get_map(self):
        return self.map
    
    def _import_file(self, file: str) -> list[list[Cell]]:
        map = []
        
        with open(file, 'r') as fp:
            
            r = 0
            
            while True:
                line = fp.readline()
                
                if not line:
                    break
                
                row = line.strip().split(' ')
                row_list: list[Cell] = []
                
                for c, value in enumerate(row):
                    value = int(value)
                    if value == 0: # white
                        row_list.append(Cell(0, False))
                        
                    if value == 1: # green
                        row_list.append(Cell(1, True))
                        
                    if value == 3: # player
                        row_list.append(Cell(3, False))
                        self.player_position.x = c
                        self.player_position.y = r
                        
                    if value == 4: # end
                        row_list.append(Cell(4, False))
                        self.objective_position.x = c
                        self.objective_position.y = r
                        
                map.append(row_list)
                r += 1
    
        return map
        
    def _check_neighbors(self, row: int, col: int) -> int:
        neighbors = 0
        
        # -1/-1  |  -1/0  | -1/+1
        #  0/-1  |    x   |  0/+1
        # +1/-1  |  +1/0  | +1/+1
        
        for r in range(row - 1, row + 2):
            for c in range(col - 1, col + 2):
                if r >= 0 and r < len(self.map) and c >= 0 and c < len(self.map[0]) and (r != row or c != col):
                    
                    alive = self.map[r][c].alive
                    if (alive):
                        neighbors += 1
                        
        return neighbors
    
    def next_step(self, map: list[list[Cell]]):
        new_map = copy.deepcopy(map)
        
        for row in range(len(new_map)):
            for col in range(len(new_map[0])):
                
                alive = new_map[row][col].alive
                
                # white
                if not alive:
                    neighbors = self._check_neighbors(row, col)
                    
                    if neighbors < self.birth_rule.lower_than and neighbors > self.birth_rule.greater_than and new_map[row][col].value != 4:
                        new_map[row][col].alive = True # green
            
                # green
                elif alive:
                    neighbors = self._check_neighbors(row, col)
                    
                    if neighbors < self.survivor_rule.lower_than and neighbors > self.survivor_rule.greater_than and new_map[row][col].value != 4:
                        new_map[row][col].alive = True # green
                        
                    else:
                        new_map[row][col].alive = False # white
        
        return new_map
    
    def step(self):
        self.map = self.next_step(self.map)
        
        if self.map[self.player_position.y][self.player_position.x].alive:
            print('game over')
    
    def move_player(self, direction: PlayerDirection):
        old_x = self.player_position.x
        old_y = self.player_position.y
        
        if direction == PlayerDirection.UP:
            self.player_position = Point(old_x, old_y - 1)
            self.map[old_y][old_x].value = 0
            self.map[old_y - 1][old_x].value = 3
            
        if direction == PlayerDirection.DOWN:
            self.player_position = Point(old_x, old_y + 1)
            self.map[old_y][old_x].value = 0
            self.map[old_y + 1][old_x].value = 3
            
        if direction == PlayerDirection.RIGHT:
            self.player_position = Point(old_x + 1, old_y)
            self.map[old_y][old_x].value = 0
            self.map[old_y][old_x + 1].value = 3
            
        if direction == PlayerDirection.LEFT:
            self.player_position = Point(old_x - 1, old_y)
            self.map[old_y][old_x].value = 0
            self.map[old_y][old_x - 1].value = 3
