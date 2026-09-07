def solution(x, n):
    
    if x == 0:
        result = [0 for _ in range(n)]
    else:
        flag = (1 if x > 0 else -1)
        result = [i for i in range(x, x*n+flag, x)]

    return result