from collections import deque

def solution(people, limit):
    sorted_people_deque = deque(sorted(people))
    boat_count = 0
    
    while sorted_people_deque:
        
        heaviest_weight = sorted_people_deque.pop()
        
        if sorted_people_deque and sorted_people_deque[0] + heaviest_weight <= limit:
            sorted_people_deque.popleft()
        
        boat_count += 1
    
    return boat_count