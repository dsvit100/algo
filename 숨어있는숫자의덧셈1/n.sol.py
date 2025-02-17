# my_string이 변수
# my_string 안의 모든 수의 합 구하기


def solution(my_string):
    answer = []
    for number in my_string:  # my_string을 반복하여 number 객체 생성
        if type(number) == str: # 만약 number 객체가 글자라면
            pass # 패스해줘
        else: #아니라면 (숫자라면)
            number.append(int(answer)) # answer에 더해줘
    return answer



print(solution('aAb1B2cC34oOp')) # => 10
print(solution('1a2b3c4d123')) # => 16