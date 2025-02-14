
def solution(n, k):
    # n : 양꼬치 인분수 / k : 음료수 개수
    answer = 0

    if n >= 10:  # 먹은 양꼬치 인분수가 10인분보다 많이 먹었다면
        service = n // 10
        answer = n * 12000 + (k - service) * 2000
    else:
        answer = n * 12000 + k * 2000  # 서비스 없이 밥을 먹었다면 먹은대로 계산

    return answer

print(solution(10, 3)) # => 124000
print(solution(64, 6)) # => 768000