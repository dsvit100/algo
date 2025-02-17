# my_string 문자열
# letter를 제거한 후 출력

def solution(my_string, letter):
    answer = []
    for char in my_string: # my_string 만큼 반복하면서 char 리스트를 만들거야
        if char in letter: # char 리스트에 letter가 포함되면
            pass # pass 해줘
        else:
            answer.append(char) # 그렇지 않다면 answer에 char를 더해줘
    return


print(solution('abcdef', 'f')) # -> "abcde"
print(solution('BCBdbe', 'B')) # -> "Cdbe"