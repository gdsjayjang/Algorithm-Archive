Y, M, D = map(int, input().split())

# Please write your code here.
season_spring = [3, 4, 5]
season_summer = [6, 7, 8]
season_fall = [9, 10, 11]
season_winter = [12, 1, 2]

day_30 = [4, 6, 9, 11]

# 윤년 체크
def yun(Y):
    if Y % 4 == 0:
        if Y % 100 == 0:
            if Y % 400 == 0:
                return True
            return False
        return True # 윤년이다.
    else:
        return False

def date_check(Y, M, D):
    # 2월일 때 먼저 체크
    if M == 2:
        if D >= 30:     # 2월 날짜가 30일 이상일 때 무조건 오류
            return False
        elif (yun(Y) != 1) and (D >=29): # 윤년이 아닌데 2월 날짜가 29일 이상
            return False
        else:
            return True

    elif M in day_30:
        if D == 31:
            return False
        else:
            return True
    else:
        return True

def season_check(M):
    if M in season_spring:
        return 'Spring'
    elif M in season_summer:
        return 'Summer'
    elif M in season_fall:
        return 'Fall'
    elif M in season_winter:
        return 'Winter'

if date_check(Y, M, D):
    res = season_check(M)
    print(res)
else:
    print(-1)