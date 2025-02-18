# 변수 = numbers
# numbers 안에 있는 수 중 두 수를 곱해 만들 수 있는 최댓값

# numbers 중에서 가장 큰 수 2개 구하기
# 두 수 곱해서 출력

# 버블정렬
# 맨 뒤의 반복문이 끝날 때까지 앞선 두 수의 크기를 비교하여 우로 정렬함
# 가장 큰게 우측으로 가서 고정(확정) 그리고 계속 반복됨

def solution(numbers):
    n = len(numbers)
    
    # .sort()
    for i in range(n):
        for j in range(0, n-i-1):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
                # 버블정렬로 j를 내 자리라 생각하고 j+1은 오른쪽으로 민다

    return numbers[-1] * numbers[-2]


print(solution([1, 2, 3, 4, 5])) # => 20
print(solution([0, 31, 24, 10, 1, 9])) # => 744