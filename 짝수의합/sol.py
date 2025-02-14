# 정수 n이 주어질 때, n이하의 짝수를 모두 더한 값을 return 하도록 solution 함수를 작성해주세요.

# n 이하 규정
# 짝수 규정
# 덧셈

def solution(n): # 값의 반복
    answer = 0

    for i in range(n+1):
        if i % 2 == 0:
            answer = answer + i # (= answer += i)

    return answer


print(solution(10))
print(solution(4))
