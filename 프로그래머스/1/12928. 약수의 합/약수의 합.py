import math

def solution(n):
    if n == 0:
        return 0
    
    answer = 0
    square_root = int(math.sqrt(n))
    
    for candidate in range(1, square_root + 1):
        
        if n % candidate == 0:
            paired_divisor = n // candidate
            
            if candidate == paired_divisor:
                answer += candidate
            else:
                answer += candidate + paired_divisor
    
    return answer
