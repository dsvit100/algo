# num_list 에 기재된 숫자를 거꾸로 뒤집은 배열 출력

def solution(num_list):
    result = []
    for num in num_list: # num_list 만큼 반복하며 num값 생성
        result.insert(0, num)
        # result에 0번째에 num값을 넣는다
        # 모든 num값이 0번째 자리로오므로, 먼저 온 num값은 우측으로 밀림
        # => 역순
    return result


print(solution([1, 2, 3, 4, 5])) # => [5, 4, 3, 2, 1]
print(solution([1, 1, 1, 1, 1, 2])) # => [2, 1, 1, 1, 1, 1]
print(solution([1, 0, 1, 1, 1, 3, 5])) # => [5, 3, 1, 1, 1, 0, 1]