N = int(input())
A = list(map(int,input().split()))
sec = [0]*N
sec[0] = 0
sec[1] = A[1]

for i in range(2,N):

    sec[i] = min(sec[i-1]+A[i], sec[i-2]+2*A[i])

print(sec[N-1])