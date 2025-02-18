# my_string이 변수
# my_string 안의 모든 수의 합 구하기


def solution(my_string):
    answer = 0
    for number in my_string:  # my_string을 반복하여 number 객체 생성
        if number.isdigit(): # 만약 number 객체가 숫자라면
            answer += int(number) # answer에 더해줘
        else:
            pass
    return answer



print(solution('aAb1B2cC34oOp')) # => 10
print(solution('1a2b3c4d123')) # => 16