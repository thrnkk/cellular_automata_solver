from map import Map, Rule, Cell
from player import Player, PlayerDirection
from solver import MazeSolver
import pygame, sys
from pygame.locals import *

map_object = Map(Rule(3, 6), Rule(1, 5))
map_object.set_map(map_object._import_file('./files/input.txt'))
player_object = Player(map_object)
maze_solver = MazeSolver()

maze_solver.solve(map_object)
maze_solver.pretty_print()
path = maze_solver.result
print(f'São necessários: {len(path)} passos para resolver.')
print(f'Foram checados {maze_solver.steps} passsos.')
print(f'Foram necessários {maze_solver.seconds} segundos para resolver.')

clock = pygame.time.Clock()

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((850, 650))
    pygame.display.set_caption('Basic Pygame program')

    # Fill background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((0, 0, 0))

    # Blit everything to the screen
    screen.blit(background, (0, 0))
    pygame.display.flip()

    # Event loop
    while True:
        for event in pygame.event.get() :
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == KEYUP:
                if event.key == K_LEFT: player_object.move(PlayerDirection.LEFT)
                if event.key == K_RIGHT: player_object.move(PlayerDirection.RIGHT)
                if event.key == K_UP: player_object.move(PlayerDirection.UP)
                if event.key == K_DOWN: player_object.move(PlayerDirection.DOWN)
                
                map_object.step()
                print(player_object.best_directions())
                    
        screen.blit(background, (0, 0))
        
        for r in range(len(map_object.map)):
            for c in range(len(map_object.map[0])):
                
                if (map_object.map[r][c].alive == False):
                    pygame.draw.rect(screen, (255, 255, 255), (c * 10, r * 10, 10, 10))
                    
                if (map_object.map[r][c].alive == True):
                    pygame.draw.rect(screen, (0, 255, 0), (c * 10, r * 10, 10, 10))
                    
                if (map_object.map[r][c].value == 3):
                    pygame.draw.circle(screen, (0, 0, 255), ((c * 10) + 5, (r * 10) + 5), 2)
                    
                if (map_object.map[r][c].value == 4):
                    pygame.draw.rect(screen, (150, 0, 0), (c * 10, r * 10, 10, 10))
                
        fps = clock.get_fps()
        pygame.display.set_caption(f'Cellular Automata: {fps} FPS')
                
        pygame.display.flip()

        clock.tick()