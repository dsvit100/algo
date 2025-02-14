def solution(n): # 값의 반복
    answer = 0

    for i in range(2, n+1, 2):
            answer = answer + i # (= answer += i)

    return answer


print(solution(10))
print(solution(4))