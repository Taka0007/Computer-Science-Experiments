N = int(input())
num = list(map(int,input().split()))
num.sort()

if len(num)%2==1:
    ans = num[ int((N-1)/2) ] 
else:
    ans = ( num[ int((N/2)-1) ] + num[ int((N/2))] )/2

print(ans)
