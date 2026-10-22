def solution(strings, n):
    return sorted(strings, key=lambda word: (word[n], word))