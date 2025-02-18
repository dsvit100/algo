# num_list 에 기재된 숫자를 거꾸로 뒤집은 배열 출력
# 

def solution(num_list):
    return num_list[::-1] # -1은 처음부터 끝까지 뒤에서부터 데이터를 역순으로 잘라서 나열


print(solution([1, 2, 3, 4, 5])) # => [5, 4, 3, 2, 1]
print(solution([1, 1, 1, 1, 1, 2])) # => [2, 1, 1, 1, 1, 1]
print(solution([1, 0, 1, 1, 1, 3, 5])) # => [5, 3, 1, 1, 1, 0, 1]