from functools import cmp_to_key

def compare(a, b):
    ab = a + b
    ba = b + a
    
    if ab > ba:
        return -1  
    elif ab < ba:
        return 1   # b가 더 커야 하니까 b를 앞으로 (양수 반환 = b가 앞)
    else:
        return 0   # 같으면 순서 상관없음


def solution(numbers):
    str_numbers = [str(num) for num in numbers]  
    
    sorted_numbers = sorted(str_numbers, key=cmp_to_key(compare))
    
    answer = ''.join(sorted_numbers)
    
    if answer[0] == '0':
        answer = '0'
    
    return answer