def solution(park, routes):
    current = []
    for i in range(len(park)):
        for j in range(len(park[0])):
            if park[i][j] == "S":
                current = [i, j]
          
    direction = "NSEW"
    dy = [-1, 1, 0, 0]
    dx = [0, 0, 1, -1]
    
    for route in routes:
        spl = route.split()
        d = spl[0]
        c = int(spl[1])
        idx = direction.index(d)
        
        ny, nx = current
        isValid = True
        
        for i in range(c):
            ny += dy[idx]
            nx += dx[idx]
        
            if (ny < 0) or (ny >= len(park)) or (nx < 0) or (nx >= len(park[0])):
                isValid = False
                break
            
            if park[ny][nx] == "X":
                isValid = False
                break
            
        if isValid:
            current = [ny, nx]
    return current