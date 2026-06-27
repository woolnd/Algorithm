def solution(wallet, bill):
    answer = 0
    
    wallet = [min(wallet), max(wallet)]
    bill = [min(bill), max(bill)]

    while wallet[0] < bill[0] or wallet[1] < bill[1]:
        if bill[0] >= bill[1]:
            bill[0] //= 2
        else:
            bill[1] //= 2
        bill = [min(bill), max(bill)]
        answer += 1
    
    return answer