# numbers의 평균값

# numbers를 모두 더하기
# numbers에 몇개가 있는지 파악하기
# 모두 더한 값에 개수 나누기


def solution(*numbers):
    answer = 0
    for i in numbers:
        i = total
        answer = sum(total) / len(numbers)
    return answer

print(solution(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)) # => 5.5
print(solution(89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99)) # => 94.0