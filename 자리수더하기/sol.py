def solution(n):
    ansswer = 0

    while n > 0:
        # a = divmod(n, 10)[0] # n //10
        # b = divmod(n, 10)[1] # n % 10
        a, b = divmod(n, 10) # divmod(a, b)a를 b로 나눈 몫과 나머지가 한꺼번에 나옴
        answer = answer + b
        n = a
    return answer

print(solution('1234'))
print(solutoin('930211'))