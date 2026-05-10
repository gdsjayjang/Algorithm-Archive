A, B, C = map(int, input().split())

if (A<B) and (A<C):
    if B>C:
        print(C)
    else:
        print(B)
elif (B<A) and (B<C):
    if A>C:
        print(C)
    else:
        print(A)
elif (C<A) and (C<B):
    if A>B:
        print(B)
    else:
        print(A)

# ABC
# ACB
# BAC
# BCA
# CAB
# CBA