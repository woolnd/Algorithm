def solution(d, budget):
    answer = 0
    
    sort_d = sorted(d)
    temp_b = budget
    for num in sort_d:
        if temp_b >= num:
            temp_b -= num
            answer += 1
            
    return answer