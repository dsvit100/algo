def solution(my_string, letter):
    answer = ''
    
    answer = my_string.replace(letter, '')
    # 앞의 old-v를 뒤의 old-v로 변경
    # 값을 바꿀 수 없으므로 값을 덮어쓰기해줌

    return answer


print(solution("abcdef", "f"))