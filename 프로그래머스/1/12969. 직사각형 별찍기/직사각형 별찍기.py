def solution(a, b):
    for i in range(0, b):
        print(f"{"*" * a}")
            
        
a, b = map(int, input().strip().split(' '))
solution(a, b)

