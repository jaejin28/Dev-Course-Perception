def solution(progresses, speeds):
    answer = []
    day = []
    for i in range(len(progresses)):
        temp = 100 - progresses[i]
        need = temp // speeds[i]
        if temp % speeds[i] == 0:
            day.append(need)
        else:
            day.append(need+1) 
    # print(day)
    
    cnt = 0
    for i in day:
        if i > cnt:
            answer.append(1)
            cnt = i
        else:
            answer[-1] += 1
    return answer