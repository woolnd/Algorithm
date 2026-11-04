def solution(k, score):
    top_score = []
    answer = []
    for s in score:
        if len(top_score) == 0 or len(top_score) < k:
            top_score.append(s)
        else:
            min_score = min(top_score)
            if min_score < s:
                index = top_score.index(min_score)
                top_score[index] = s

        answer.append(min(top_score))
    return answer