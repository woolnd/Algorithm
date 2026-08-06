import heapq

def solution(n, k, enemy):
    if len(enemy) == k:
        return k
    
    answer = 0
    heap = []
    check_n = n
    check_k = k
    
    for i in range(len(enemy)):
        if check_n < enemy[i] and check_k > 0:
            if len(heap) > 0:
                tmp = -heapq.heappop(heap)
                
                if tmp > enemy[i]:
                    check_n += tmp
                    heapq.heappush(heap, -enemy[i])
                    check_n -= enemy[i]     
                else:
                    heapq.heappush(heap, -tmp)
            check_k -= 1
            
        elif check_n >= enemy[i]:
            heapq.heappush(heap, -enemy[i])
            check_n -= enemy[i]  
        else:
            break
            
        answer += 1
    return answer
