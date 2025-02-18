def solution(n):
    answer = 0
    for i in str(n): # for문은 시퀀스형 자료들만 돌릴 수 있음 (숫자 불가)
        answer = answer + int(i)

    return answer


print(solution(1234))
print(solution(930211))