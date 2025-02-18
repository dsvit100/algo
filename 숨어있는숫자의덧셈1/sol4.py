def solution(my_string):
    answer = 0

    for char in my_string:
        try:
            answer += int(char)
        except:
            continue # 다음 for문으로 넘어가줘

    return answer

print(solution("aAb1B2cC34oOp"))