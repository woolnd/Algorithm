def solution(n):
    str_n = str(n)
    answer = [int(str_n[i]) for i in range(len(str_n) - 1, -1, -1)]
    return answer