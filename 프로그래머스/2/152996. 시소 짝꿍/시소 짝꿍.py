def solution(weights):
    answer = 0
    counter = {}
    ratios = [(2,3),(2,4),(3,2),(3,4),(4,2),(4,3)]
    
    for w in weights:
        same = counter.get(w, 0)
        answer += same
        
        for (a, b) in ratios:
            if w * a % b == 0:
                partner = w * a // b
                answer += counter.get(partner, 0)
        counter[w] = counter.get(w, 0) + 1       
        
    return answer