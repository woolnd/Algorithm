import math

def solution(left, right):
    answer = 0
    
    for number in range(left, right + 1):
        square_root = math.isqrt(number)
        
        if square_root * square_root != number:
            answer += number
        elif square_root * square_root == number:
            answer -= number
            
    return answer