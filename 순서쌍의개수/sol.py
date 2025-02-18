# (a * b) = n 이 될 수 있는 모든 두 수
# 모든 공약수의 개수구하기

def solution(n):
    answer = 0

    for num in range(1, n+1):
        if n % num == 0:
            answer += 1

    return answer


print(solution(20)) # => 6
print(solution(100)) # => 9