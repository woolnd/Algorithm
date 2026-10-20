from itertools import combinations

def solution(numbers):
    comb_list = list(combinations(numbers, 2))
    answer = []
    
    for comb in comb_list:
        answer.append(comb[0] + comb[1])
    
    return sorted(set(answer))