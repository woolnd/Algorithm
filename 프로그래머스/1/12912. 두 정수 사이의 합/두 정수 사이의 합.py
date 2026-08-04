def solution(a, b):
    if a == b:
        return a
    else:
        if a > b:
            return sum(range(b, a+1))
        else:
            return sum(range(a, b+1))
            