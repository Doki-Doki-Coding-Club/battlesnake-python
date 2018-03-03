import numpy as np

import game_state 

def flood_fill(data, max_depth):
    board = data.baord[:]
    snake = data.thissnake
    right = find_next_move(data, board, snake.head[0]+1, snake.head[1], max_depth)
    left = find_next_move(data, board, snake.head[0]-1, snake.head[1], max_depth)
    up = find_next_move(data, board, snake.head[0], snake.head[1]-1, max_depth)
    down = find_next_move(data, board, snake.head[0], snake.head[1]+1, max_depth)
    
    return ["right", "left", "up", "down"][argmax([right, left, up, down])]


def find_next_move(data, board, x, y, depth):
        if depth <= 0:
            return 0

        board[x,y] = 3
        
        if data.thissnake.tail is not data.thissnake.body[-2]:
            board[data.thissnake.tail[0], data.thissnake.tail[1]] = 0
        
        if x < 0 or y < 0 or x > board.shape[0] or y > board.shape[1]:
            return -3
        if board[x,y] >= 2 and [x, y] not in data.alltails():
            return -3
        
        right = find_next_move(data, board, x+1, y, depth-1) + 1
        left = find_next_move(data, board, x-1, y, depth-1) + 1
        up = find_next_move(data, board, x, y-1, depth-1) + 1
        down = find_next_move(data, board, x, y+1, depth-1) + 1
        
        return ["right", "left", "up", "down"][argmax([right, left, up, down])]
