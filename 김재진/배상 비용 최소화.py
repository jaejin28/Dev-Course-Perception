def solution(no, works):
    result = 0

    while no > 0:
        works.sort(reverse = True)
        # print(works)
        if works[0] == 0:
            break
        works[0] -= 1
        no -= 1
        # print(works,no)
    
    for i in works:
        result += i * i
        
    return result