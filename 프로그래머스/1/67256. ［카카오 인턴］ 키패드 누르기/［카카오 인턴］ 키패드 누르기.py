def solution(numbers, hand):
    answer = ''
    
    keypad = {
        '1': (0, 0), '2': (0, 1), '3': (0, 2),
        '4': (1, 0), '5': (1, 1), '6': (1, 2),
        '7': (2, 0), '8': (2, 1), '9': (2, 2),
        '*': (3, 0), '0': (3, 1), '#': (3, 2),
    }
    
    left_hand = keypad['*']   
    right_hand = keypad['#']  

    def dist(a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])
    
    for number in numbers:
        target = keypad[str(number)]
    
        if target[1] == 0:
            left_hand = target
            answer += 'L'
            continue
        elif target[1] == 2:
            right_hand = target
            answer += 'R'
            continue
    
        left_dist = dist(left_hand, target)
        right_dist = dist(right_hand, target)
    
        if left_dist == right_dist:
            chosen = hand
        elif left_dist < right_dist:
            chosen = 'left'
        else:
            chosen = 'right'
    
        if chosen == 'left':
            left_hand = target
            answer += 'L'
        else:
            right_hand = target
            answer += 'R'
            
    return answer