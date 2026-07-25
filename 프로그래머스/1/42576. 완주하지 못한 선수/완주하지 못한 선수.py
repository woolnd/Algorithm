def solution(participant, completion):
    dict = {}
    
    for name in completion:
        if name in dict.keys():
            dict[name] += 1
        else:
            dict[name] = 1
    
    for name in participant:
        if name not in dict.keys() or (dict[name] == 0):
            return name
        else:
            dict[name] -= 1