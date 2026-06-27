def solution(data, ext, val_ext, sort_by):
    answer = []

    if ext == 'code':
        mask = 0
    elif ext == 'date':
        mask = 1
    elif ext == 'maximum':
        mask = 2
    else:
        mask = 3
        
    for info in data:
        if info[mask] < val_ext:
            answer.append(info)
            
    if sort_by == 'code':
        mask = 0
    elif sort_by == 'date':
        mask = 1
    elif sort_by == 'maximum':
        mask = 2
    else:
        mask = 3
        
    answer.sort(key=lambda x: x[mask])
    
    return answer