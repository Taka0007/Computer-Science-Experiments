def f(N):
    return N*(N*(N+1)+2)+3

N = int(input())

left  = 0
right = 100

while abs(left-right) > 0.0001:
    mid = (left+right)/2

    if f(mid)>N:
        right = mid
    else:
        left = mid

print(left)
