a, b, c = map(int, input().split())
if a==b==c: 
    print(10000 + a*1000)
elif (a==b and a!=c): 
    print(1000+a*100)
elif (a==c and a != b): 
    print(1000+a*100)
elif (b==c and a !=b): 
    print(1000+b*100)
else: 
    print(max([a,b,c])*100)


# # short coding
# a, b, c = sorted(input().split())
# print(['1'+b,c][a<b<c]+'000'[a<c:])