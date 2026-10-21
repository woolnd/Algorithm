def solution(food):
    left = ''
    right = ''
    
    food_count = len(food)
    
    for i in range(1, food_count):
        count = int(food[i] / 2)
        left += str(i) * count   
        
    right = sorted(left, reverse=True)
    left += '0'
    return left + ''.join(right)