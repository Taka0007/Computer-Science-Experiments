N,K = map(int,input().split())
num = list(map(int,input().split()))
ans = 0

for i in num:
    ans += 2**(i)

print(ans)
