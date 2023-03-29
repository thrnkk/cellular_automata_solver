from enum import Enum

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

class PlayerDirection(Enum):
    UP = 'U'
    DOWN = 'D'
    RIGHT = 'R'
    LEFT = 'L'