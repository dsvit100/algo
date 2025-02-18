# n 의 각 자리 숫자의 합이 나오도록
# n을 한자리 숫자로 각각 나눠야
# 각 자리의 숫자를 뽑아야 함


def solution(n):
    return sum(map(int, list(str(n))))

# 1. str(n) = 1234 => '1','2','3','4'
# 2. list => ('1', '2', '3', '4')
# 3. map(int,list) => list를 모두 int 함수 적용 => (1, 2, 3, 4)
# 4. sum(1, 2, 3, 4)

print(solution(1234))
print(solution(930211))