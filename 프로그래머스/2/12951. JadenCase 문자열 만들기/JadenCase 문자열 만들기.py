def solution(s):
    word_list = s.split(" ")
    converted_word_list = []
    
    for word in word_list:
        converted_word = word[:1].upper() + word[1:].lower()
        converted_word_list.append(converted_word)
        
    answer = " ".join(converted_word_list)
    return answer