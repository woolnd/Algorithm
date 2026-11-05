def solution(n):
    
    if n == 1:
        return 1
    elif n == 2:
        return 2
    count_list = [0] * n
    count_list[0] = 1
    count_list[1] = 2
    
    for i in range(2, n):
        count_list[i] = count_list[i-1] + count_list[i-2]
        
    return int(count_list[-1] % 1234567)
