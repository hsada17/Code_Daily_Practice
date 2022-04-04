
# DFS/BFS Q14 특정 거리의 도시 찾기
# https://www.acmicpc.net/problem/18352

import sys
from collections import deque

# 설정 값 입력 받기
n,m,k,x = map(int, sys.stdin.readline().split())

# 도시 그래프 설정
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)

# 최단 거리 설정
distance = [-1] * (n+1)
distance[x] = 0

# bfs
q = deque()
q.append(x)

while q:
    current = q.popleft()
    # 처음 방문하는 도시일 경우 현재 도시의 최단 거리 +1을 해준다.
    for next in graph[current]:
        if distance[next] == -1:
            q.append(next)
            distance[next] = distance[current] + 1

# 최단 거리가 k값과 일치 하는 경우 출력, 일치 하는 값이 없으면 -1 출력.
check = False
for i in range(1,n+1):
    if distance[i]==k:
        print(i)
        check = True
if check == False:
    print(-1)