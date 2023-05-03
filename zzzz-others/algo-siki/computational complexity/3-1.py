import math

N = int(input())
num = list(map(int,input().split()))

ans = max(num) - min(num)

print(ans)
