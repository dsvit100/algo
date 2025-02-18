# num_list 에 기재된 숫자를 거꾸로 뒤집은 배열 출력

def solution(num_list):
    num_list.reverse() # reverse는 값을 바꿈
    return num_list


print(solution([1, 2, 3, 4, 5])) # => [5, 4, 3, 2, 1]
print(solution([1, 1, 1, 1, 1, 2])) # => [2, 1, 1, 1, 1, 1]
print(solution([1, 0, 1, 1, 1, 3, 5])) # => [5, 3, 1, 1, 1, 0, 1]