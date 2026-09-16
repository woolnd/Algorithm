def solution(absolutes, signs):
    answer = 0
    
    for i, num in enumerate(absolutes):
        sign = signs[i]
        
        if sign:
            answer += num
        else:
            answer -= num
    return answer