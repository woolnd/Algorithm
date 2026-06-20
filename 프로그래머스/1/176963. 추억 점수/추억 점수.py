def solution(name, yearning, photo):
    answer = []
    
    dict = {}
    
    for i in range(len(name)):
        dict[name[i]] = yearning[i]
    
    for names in photo:
        total = 0
        for name in names:
            total += dict.get(name, 0)

        answer.append(total)
        
    return answer