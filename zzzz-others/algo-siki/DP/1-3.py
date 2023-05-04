import math

N = int(input())
ans = [1]*N
ans[0] = 1

#2段目以降
for i in range(1,N):
    if i==1:
        ans[i] = 2
    else:
        ans[i] = ans[i-2] + ans[i-1]

print(ans[N-1])
