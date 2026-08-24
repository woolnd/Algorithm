from collections import deque

def solution(players, m, k):
    answer = 0
    alive = 0
    history = deque() 
    
    for hour, player in enumerate(players):
        while history and hour - history[0][0] >= k:
            expired_time, expired_count = history.popleft()
            alive -= expired_count
        
        if player < m:
            continue
        
        need = player // m
        
        if alive < need:
            add = need - alive
            answer += add          
            alive += add           
            history.append((hour, add))
    
    return answer