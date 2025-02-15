# num1, num2 변수
# num1 / num2 * 1000


def solution(num1, num2):
    answer = num1 / num2 * 1000 // 1
    return answer

print(solution(3, 2))
print(solution(7, 3))
print(solution(1, 16))
