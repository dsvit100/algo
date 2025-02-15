# 예각 : 0 < angle < 90
# 직각 : angle = 90
# 둔각 : 90 < angle < 180
# 평각 : angle = 180

def solution(angle):
    answer = 0
    if angle < 90:
        return 1
    if angle == 90:
        return 2
    if angle > 90:
        if angle < 180:
            return 3
    if angle == 180:
        return 4
        

print(solution(70)) # => 1
print(solution(91)) # => 3
print(solution(180)) # => 4