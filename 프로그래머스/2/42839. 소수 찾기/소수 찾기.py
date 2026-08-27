from itertools import permutations

def is_prime_number(number):
    if number < 2:
        return False
    
    for div in range(2, number):
        if number % div == 0:
            return False
    
    return True

def solution(numbers):
    answer = 0
    all_perm = set()
    
    for length in range(1, len(numbers) + 1):
        for perm in permutations(numbers, length):
            perm_str = ''.join(map(str, perm))
            all_perm.add(int(perm_str))
            
    for perm in all_perm:
        if is_prime_number(perm):
            answer += 1
        
    return answer
