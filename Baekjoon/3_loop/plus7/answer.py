T = int(input())

for i in range(T):
   a, b = map(int, input().split())
   sum = a+b
   print(f'Case #{i+1}:',a, '+', b, '=', sum)


# # short coding
# for a,_,c,_ in[*open(i:=0)][1:]:
#     i+=1
    
# print(f'Case #{i}:',a,'+',c,'=',int(a)+int(c))