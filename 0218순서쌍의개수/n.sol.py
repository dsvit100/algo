# (a * b) = n 이 될 수 있는 모든 두 수
# a와 b의 공배수

def solution(n):
    answer = 0
    for number in range(1, n+1): # 1~n까지 반복하며 number를 뽑아줘
        if number % n == 0: # 근데 number가 n으로 나눴을 때 나머지가 0이라면 (n이 number의 배수라면)
            answer += 1 # answer에 카운팅해줘
    return answer


print(solution(20)) # => 6
print(solution(100)) # => 9