def solution(a, b, n):
    answer = 0
    
    while n >= a:
        received = (n // a) * b
        remainder = n % a
        answer += received
        n = received + remainder
    return answer
