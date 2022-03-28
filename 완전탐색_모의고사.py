
# https://programmers.co.kr/learn/courses/30/lessons/42840

def solution(answers):
    stu1 = [1,2,3,4,5]
    stu2 = [2,1,2,3,2,4,2,5]
    stu3 = [3,3,1,1,2,2,4,4,5,5]

    scores = [0,0,0]
    result = []

    for idx, ans in enumerate(answers):
        if ans == stu1[idx%len(stu1)]:
            scores[0]+=1
        if ans == stu2[idx%len(stu2)]:
            scores[1]+=1
        if ans == stu3[idx%len(stu3)]:
            scores[2]+=1

    maxScore = max(scores)
    for idx,score in enumerate(scores):
        if maxScore==score:
            result.append(idx+1)

    return result
