N = int(input())
num = list(map(int,input().split()))

ans = sum(num) - min(num)
print(ans)
