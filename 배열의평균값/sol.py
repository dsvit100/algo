# 정수 배열 numbers가 매개변수로 주어집니다.
# numbers의 원소의 평균값을 return하도록 solution 함수를 완성해주세요.


# 리스트의 모든 값을 다 더해서
# 리스트 개수만큼 나누자

def solution(numbers):
    answer = 0
    answer = sum(numbers) / len(numbers)
    return answer

print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])) # => 5.5
print(solution([89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99])) # => 94.0
