def solution(n, lost, reserve):
    
    both = set(lost) & set(reserve)
    lost = sorted(set(lost) - both)
    reserve = sorted(set(reserve) - both)
    
    answer = n - len(lost)
    
    for i in lost:
        if i - 1 in reserve:
            reserve.remove(i-1)
            answer += 1
            continue
        elif i + 1 in reserve:
            reserve.remove(i+1)
            answer += 1
            continue
            
    return answer