# (a * b) = n 이 될 수 있는 모든 두 수
# 모든 공약수의 개수구하기
# 중간 값(대칭이 되는 값)을 루트 씌워주면 됨

# from math import sqrt 
def solution(n):
    answer = 0

    for num in range(1, int(n ** 0.5) + 1): # n의 1/2 = 루트 n
        if n % num == 0:
            answer += 2

            if num * num == n:
                answer -= 1

    return answer


print(solution(20)) # => 6
print(solution(100)) # => 9