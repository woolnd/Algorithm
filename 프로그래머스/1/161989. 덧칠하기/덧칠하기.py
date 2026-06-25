def solution(n, m, section):
    answer = 1
    painted = section[0] + m - 1
    
    for s in section[1:]:
        if s > painted:
            answer += 1
            painted = s + m - 1
    
    return answer