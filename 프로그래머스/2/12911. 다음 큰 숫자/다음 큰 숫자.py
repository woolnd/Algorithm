def count_ones(n):
    count = 0
    while n:
        n &= n - 1
        count += 1
    return count
        
    
def solution(n):
    n_count = count_ones(n)
    temp = n + 1
    while True:
        temp_count = count_ones(temp)
        if n_count == temp_count:
            return temp
        else:
            temp += 1
            
    return -1