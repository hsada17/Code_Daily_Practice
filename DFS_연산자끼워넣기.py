
# DFS/BFS Q18 연산자 끼워넣기
# https://www.acmicpc.net/problem/14888

import sys

n = int(input())
nums = list(map(int, sys.stdin.readline().split()))
add, sub, mul, div = map(int, sys.stdin.readline().split())

large = -1e9
small = 1e9

def dfs(idx, now):
    global large, small, add, sub, mul, div

    if idx == n:
        large = max(large, now)
        small = min(small, now)

    else:
        if add > 0:
            add -= 1
            dfs(idx+1, now + nums[idx])
            add += 1
        if sub > 0:
            sub -= 1
            dfs(idx+1, now - nums[idx])
            sub += 1
        if mul > 0:
            mul -= 1
            dfs(idx+1, now * nums[idx])
            mul += 1
        if div > 0:
            div -= 1
            dfs(idx+1, int(now / nums[idx]))
            div += 1

dfs(1, nums[0])
print(large)
print(small)