
# DFS/BFS Q19 감시 피하기
# https://www.acmicpc.net/problem/18428

import sys
from itertools import combinations

input = sys.stdin.readline

n = int(input())
grid = []
teachers = []
empty = []

for i in range(n):
    grid.append(list(input().split()))
    for j in range(n):
        if grid[i][j] == 'T':
            teachers.append([i, j])
        elif grid[i][j] == "X":
            empty.append([i, j])

# 장애물 설치 후 학생 발칵 되는지 확인. 학생 발견시 True, 미발견시 False
def check(x, y, direction):
    # direction (상, 하, 좌, 우)
    if direction == 0:
        while x >= 0:
            if grid[x][y] == 'S':
                return True
            elif grid[x][y] == 'O':
                return False
            x -= 1
    if direction == 1:
        while x < n:
            if grid[x][y] == 'S':
                return True
            elif grid[x][y] == 'O':
                return False
            x += 1
    if direction == 2:
        while y >= 0:
            if grid[x][y] == 'S':
                return True
            elif grid[x][y] == 'O':
                return False
            y -= 1
    if direction == 3:
        while y < n:
            if grid[x][y] == 'S':
                return True
            elif grid[x][y] == 'O':
                return False
            y += 1
    return False

# 각 선생님마다 학생 발칵 되는지 확인
def watchTeacher():
    for x,y in teachers:
        for i in range(4):
            if check(x,y,i):
                return True
    return False

answer = False

# 장애물 설치 후 체커 돌리기

for selected in combinations(empty, 3):
    # 장애물 설치
    for x,y in selected:
        grid[x][y] = "O"

    # 설치 후 확인
    if not watchTeacher():
        answer = True
        break

    # 장애물 철거
    for x,y in selected:
        grid[x][y] = "X"

if answer:
    print("YES")
else:
    print("NO")