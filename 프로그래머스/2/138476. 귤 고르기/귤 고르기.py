from collections import defaultdict

def solution(k, tangerine):
    dict = defaultdict(int)
    
    for key in tangerine:
        dict[key] += 1
    
    size_count = dict.values()
    
    total = 0
    count = 0
    for size in sorted(size_count, reverse=True):
        total += size
        count += 1
        if total >= k:
            return count
    
    return -1