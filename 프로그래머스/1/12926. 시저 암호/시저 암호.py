def solution(s, n):
    answer = ''
    
    for char in s:
        if ord(char) >= 65 and ord(char) <= 90:
            before = ord(char) - 65 + n
            after = before % 26 + 65
            answer += chr(after)
        elif ord(char) >= 97 and ord(char) <= 122:
            before = ord(char) - 97 + n
            after = before % 26 + 97
            answer += chr(after)
        else:
            answer += char
        
    return answer