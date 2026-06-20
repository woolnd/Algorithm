def solution(name, yearning, photo):
    answer = []
    
    score_map = {}
    for i in range(len(name)):
        score_map[name[i]] = yearning[i]
    
    for names in photo:
        total = 0
        
        for name in names:
            total += score_map.get(name, 0)
            
        answer.append(total)
        
    return answer