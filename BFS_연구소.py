
# DFS/BFS Q15 연구소
# https://www.acmicpc.net/problem/14502

import sys
import copy
from collections import deque
from itertools import combinations

n, m = map(int, sys.stdin.readline().split())
grid = []
empty = []
virus_q = deque()

# 빈 공간 리스트 담기, 그리드 만들기
for i in range(n):
    nums = list(map(int, sys.stdin.readline().split()))
    grid.append(nums)
    for idx, val in enumerate(nums):
        if val == 0:
            empty.append([i, idx])
        elif val == 2:
            virus_q.append([i, idx])

# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 바이러스 확산 체크 함수
def virusSpread(x, y, gridcopy):
    if x >= n or x < 0 or y >= m or y < 0:
        return False
    if gridcopy[x][y] == 0:
        return True
    else:
        return False

maxProtect = 0

# 빈 공간 벽 세우는 조합 구하기
for selection in list(combinations(empty, 3)):
    cnt = 0
    grid_copy = copy.deepcopy(grid)
    virus_copy = copy.deepcopy(virus_q)

    # 빈 공간에 벽 세우기
    for each in selection:
        x, y = each
        grid_copy[x][y] = 1

    # 바이러스 확산 시키기
    while virus_copy:
        position_x, position_y = virus_copy.popleft()

        # 방향 4개: 상, 하, 좌, 우
        for i in range(4):
            tmp_x = position_x + dx[i]
            tmp_y = position_y + dy[i]
            if virusSpread(tmp_x, tmp_y, grid_copy):
                grid_copy[tmp_x][tmp_y] = 2
                virus_copy.append([tmp_x, tmp_y])

    # 바이러스 청정 지역 카운트
    for row in grid_copy:
        for val in row:
            if val == 0:
                cnt += 1

    maxProtect = max(maxProtect, cnt)

print(maxProtect)