from collections import Counter

def solution(s):
    answer = True
    
    s = s.lower()
    count = Counter(s)
    p_count = count['p']
    y_count = count['y']
    
    if p_count == y_count:
        return True    
    else:
        return False
