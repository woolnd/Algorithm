def solution(s):
    sorted_char = sorted(s, reverse=True)
    return ''.join(sorted_char)