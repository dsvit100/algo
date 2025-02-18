def solution(my_string, letter): 
    answer = ''
    for char in my_string:
        if char != letter: # char에 letter 문자가 없니?
            answer += char # 없으면 answer에 더해줘

    return answer


print(solution("abcdef", "f"))