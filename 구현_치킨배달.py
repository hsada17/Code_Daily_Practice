
# 치킨 배달
# https://www.acmicpc.net/problem/15686

from itertools import combinations

# 도시 크기 n 입력 값과 치킨 점포 최대 개수 m 받기
n, m = map(int, input().split())

# 반복문을 n번 만큼 돌리면서 치킨 점포와 집의 좌표 각각 리스트에 받기
chicken = []
house = []
for row in range(1, n+1):
    a = list(map(int, input().split()))
    for idx, column in enumerate(a):
        if column == 1:
            house.append([row,idx+1])
        elif column == 2:
            chicken.append([row,idx+1])

# 치킨거리 계산 함수
def chickenCheck(house, selection):
    cnt = 0
    for each in house:
        small_dist = 1000
        for store in selection:
            small_dist = min((abs(each[0]-store[0])+abs(each[1]-store[1])),small_dist)
        cnt += small_dist
    return cnt

dist = 999999999

# combination 메소드를 이용하여 치킨점포 조합을 구하고,
# 각 조합마다 최소 치킨거리 계산한다. 모든 조합 중에서의 최소값을 dist로 저장
for selection in combinations(chicken,m):
    dist = min(chickenCheck(house, selection),dist)

print(dist)