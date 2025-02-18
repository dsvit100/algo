# 변수 = numbers
# numbers 안에 있는 수 중 두 수를 곱해 만들 수 있는 최댓값

# numbers 중에서 가장 큰 수 2개 구하기
# 두 수 곱해서 출력



def solution(numbers):
    numbers.sort()
    return numbers[-1] * numbers[-2] # 제일 마지막에서 첫번째 숫자 접근 = -1


print(solution([1, 2, 3, 4, 5])) # => 20
print(solution([0, 31, 24, 10, 1, 9])) # => 744