def solution(today, terms, privacies):
    answer = []
    
    ty, tm, td = today.split('.')
    today_days = (int(ty) * 12 * 28) + (int(tm) * 28) + int(td)
    
    term_dict = {}
    
    for term in terms:
        term_split = term.split()
        term_dict[term_split[0]] = int(term_split[1]) * 28
        
    for index, privacy in enumerate(privacies, 1):
        privacy_split = privacy.split()
        y, m, d = map(int, privacy_split[0].split('.'))
        days = (y * 12 * 28) + (m * 28) + d
        days += term_dict[privacy_split[1]]
        
        if today_days >= days:
            answer.append(index)
        else:
            continue
        
    return answer