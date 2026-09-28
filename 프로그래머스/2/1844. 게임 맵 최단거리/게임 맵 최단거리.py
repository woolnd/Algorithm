from collections import deque

def solution(maps):
    answer = 0
    
    dy = [1, -1, 0, 0]
    dx = [0, 0, -1, 1]
    
    len_row = len(maps)
    len_col = len(maps[0])
    
    visited = [[False] * len_col for _ in range(0, len_row)]
    visited[0][0] = True
    
    queue = deque([(0, 0, 1)])
    
    while queue:
        y, x, distance = queue.popleft()
        
        if y == len_row - 1 and x == len_col - 1:
            return distance
        
        for i in range(0, 4):
            ny = y + dy[i]
            nx = x + dx[i]
            
            if ny < 0 or ny >= len_row or nx < 0 or nx >= len_col:
                continue
            if visited[ny][nx]:
                continue
            if maps[ny][nx] == 0:
                continue
            
            queue.append((ny, nx, distance+1))
            visited[ny][nx] = True
        
    return -1