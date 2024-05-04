'''
priorities의 최댓값(=우선 순위)을 저장
맨 앞에 값 빼고, location -= 1

popleft값이 우선 순위가 아니면 append
location이 음수면 타켓이 맨 뒤로 간 거니까 queue길이 -1

popleft값이 우선 순위면 answer += 1
location이 음수면 타켓이 빠진 거니까 break
'''
from collections import deque

def solution(priorities, location):    
    answer = 0
    queue = deque(priorities)
    while queue:
        m = max(queue)
        f = queue.popleft()
        location -= 1
        if m != f:
            queue.append(f)
            if location < 0:
                location = len(queue) - 1
        else:
            answer += 1
            if location < 0:
                break
    return answer