def solution(wallpaper):
    min_val = float('inf')   
    max_val = float('-inf')  

    position = []
    lux = min_val
    luy = min_val
    rdx = max_val
    rdy = max_val
    
    for row, line in enumerate(wallpaper):
        for col, char in enumerate(line):
            if char == '#':
                position.append((row, col))
                
    for (row, col) in position:
        lux = min(lux, row)
        luy = min(luy, col)
        
        rdx = max(rdx, row)
        rdy = max(rdy, col)
        
    return (lux, luy, rdx+1, rdy+1)