

def solution(cacheSize, cities):
    answer = 0
    cache = []
    
    if cacheSize == 0:
        return len(cities) * 5
    
    for city in cities:
        city = city.lower()
        if city in cache:
            cache.remove(city)
            cache.append(city)
            
            answer += 1
        else:
            if len(cache) == cacheSize:
                tmp = cache[0]
                cache.remove(tmp)
                cache.append(city)
            else:
                cache.append(city)
            
            answer += 5
    return answer