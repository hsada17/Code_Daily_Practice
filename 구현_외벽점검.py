
# 외벽 점검
# https://programmers.co.kr/learn/courses/30/lessons/60062

def solution(n, weak, dist):
    from itertools import permutations

    length = len(weak)

    # 원을 선형으로 만들어주기
    weak = weak + [w+n for w in weak]

    answer = len(dist)+1 # 초기 최소 인원 설정을 가능한 최댓값 (dist값) 보다 1 큰 수로 할당

    for start in range(length):
        # 각 거리 조합마다 반복문 돌리기
        for combination in permutations(dist, len(dist)):
            count = 1 # 투입된 친구 수
            position = weak[start] + combination[count-1] # 끝 지점

            # 끝 지점과 weak 포인트 지점을 비교하여, weak 포인트가 더 크다면 친구 한명 더 투입하는 반복문
            for i in range(start, start+length)
                if position < weak[i]:
                    count+=1
                    if count > len(dist):
                        break
                    position = weak[i] + combination[count-1]
            answer = min(count,answer)

    if answer > len(dist):
        return -1
    return answer

print(solution(12, [1, 5, 6, 10], [1, 2, 3, 4]))