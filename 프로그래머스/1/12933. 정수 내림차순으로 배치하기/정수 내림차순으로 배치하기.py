def solution(n):
    answer = []
    
    for i in str(n):
        answer.append(int(i))
    
    answer.sort(reverse=True)
    result = int(''.join(map(str, answer)))
    return result