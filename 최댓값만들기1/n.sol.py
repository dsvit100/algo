# 변수 = numbers
# numbers 안에 있는 수 중 두 수를 곱해 만들 수 있는 최댓값

# numbers 중에서 가장 큰 수 2개 구하기
# 두 수 곱해서 출력



def solution(numbers):
    result = 0
    numbers.sorted(reverse=True) # numbers를 역순으로 정렬하여 새 리스트 생성
    result = numbers[0] * numbers[1] # numbers의 0번째 * 1번째
    return result


print(solution([1, 2, 3, 4, 5])) # => 20
print(solution([0, 31, 24, 10, 1, 9])) # => 744
