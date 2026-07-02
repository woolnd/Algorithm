def solution(players, callings):
    n = len(players)

    rank_to_name = [None] + players[:]  
    name_to_rank = {name: i + 1 for i, name in enumerate(players)}

    for name in callings:
        rank = name_to_rank[name]
        prev_rank = rank - 1
        prev_name = rank_to_name[prev_rank]

        name_to_rank[name] = prev_rank
        name_to_rank[prev_name] = rank
        rank_to_name[prev_rank] = name
        rank_to_name[rank] = prev_name

    return rank_to_name[1:]