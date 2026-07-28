def solution(rows, columns, queries):
    matrix = [[c + r*columns for c in range(1, columns+1)] for r in range(rows)]
    answer = []
    
    for x1, y1, x2, y2 in queries:
        coords = []
        
        for y in range(y1, y2+1):
            coords.append((x1, y))
        for x in range(x1+1, x2+1):
            coords.append((x, y2))
        for y in range(y2-1, y1-1, -1):
            coords.append((x2, y))
        for x in range(x2-1, x1, -1):
            coords.append((x, y1))
            
            
        values = [matrix[x-1][y-1] for x, y in coords]
        values = [values[-1]] + values[:-1]
        for (x, y), v in zip(coords, values):
            matrix[x-1][y-1] = v
            
        answer.append(min(values))
        
    return answer