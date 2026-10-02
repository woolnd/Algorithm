def solution(s):
    answer = []
    word_list = s.split(' ')
    
    for word in word_list:
        flag = True
        temp = ''
        for char in word:
            if flag == True:
                temp += char.upper()
                flag = False
            else:
                temp += char.lower()
                flag = True
        answer.append(temp)
    
    return ' '.join(answer)