def solution(my_string):
    answer = 0
# 아스키코드를 확인하여 글자 범위를 만들어줌
# ord는 글자를 컴퓨터 글자로 변경해줌

    for char in my_string:
        if not (ord('A') <= ord(char) <= ord('z')):
            answer += int(char)

    return answer


print(solution("aAb1B2cC34oOp"))
