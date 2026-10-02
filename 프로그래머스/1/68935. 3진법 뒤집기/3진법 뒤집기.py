def solution(n):
    num = n
    num_list = []
    
    while num / 3 != 0:
        num_list.append(num%3)
        num = int(num/3)
        
    answer = 0
    num_len = len(num_list) - 1
    for ind, i in enumerate(range(num_len, -1, -1)):
        answer += num_list[ind] * (3 ** i)
    
    return answer