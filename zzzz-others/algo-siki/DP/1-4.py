# N=1の時でも対応できるように配列サイズを多めに取っている
# この操作を忘れるとN=1の時にans[1]が定義できずにエラーを吐く

N = int(input())
ans = [0]*(N+5)
ans[0] = 1
ans[1] = 2
ans[2] = 4

if N>=3:
    for i in range(3,N):
        ans[i] = ans[i-1] + ans[i-2] + ans[i-3]

print(ans[N-1])
