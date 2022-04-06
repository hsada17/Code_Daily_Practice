
# DFS/BFS Q16 경쟁적 전염
# https://www.acmicpc.net/problem/18405

import sys
from collections import deque

# 그리드 길이 값과 바이러스 아이디 최대 숫자 받기
n, k = map(int, sys.stdin.readline().split())

grid = []

# 바이러스 위치 담을 큐 생성
virus_q = deque()
for _ in range(k):
    virus_q.append([])

# 그리드에 입력 값 받기
for row in range(n):
    nums = list(map(int, sys.stdin.readline().split()))
    grid.append(nums)
    # 바이러스 큐에 위치 값 받기
    for col, val in enumerate(nums):
        if val != 0:
            virus_q[val-1].append([row, col])

# s,x,y 입력 값 받기
s, x, y = map(int, sys.stdin.readline().split())

# 바이러스 전파 될 [상, 하, 좌, 우] 경로 좌표 설정
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 바이러스 전파 시키는 반복문
while s > 0:

    # 바이러스 큐에서 아이디 하나 씩 꺼내기
    for virus_num in range(k):
        current_virus = virus_q.popleft()

        # 전파 된 바이러스 위치 값 넣을 tmp 리스트 생성
        tmp = []

        # 상,하,좌,우로 좌표를 바꾸어 가며 그리드에 값이 0일 경우 전파시키고, tmp에 좌표 넣기
        for current_location in current_virus:
            v_x, v_y = current_location
            for i in range(4):
                tmp_x = v_x + dx[i]
                tmp_y = v_y + dy[i]
                if tmp_x <0 or tmp_x >= n or tmp_y <0 or tmp_y >= n:
                    continue
                if grid[tmp_x][tmp_y] == 0:
                    grid[tmp_x][tmp_y] = virus_num+1
                    tmp.append([tmp_x, tmp_y])

        # 해당 바이러스 아이디 전파가 끝나면 큐에 이번 초에 전파된 좌표 값 넣기
        virus_q.append(tmp)

    # 초 줄여주기
    s -= 1

print(grid[x-1][y-1])