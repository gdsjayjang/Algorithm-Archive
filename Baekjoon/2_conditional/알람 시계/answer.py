# 방법 1.
h, m = map(int, input().split())
if m >=45: 
    print(h, m-45)
else: 
    print(h-1 if h !=0 else 23, 60+m-45)
    
# # 방법 2.
# h, m = map(int, input().split())
# print((h-(m<45))%24, (m-45)%60)