def solve(N):
    if N > 0:
        ans = 'positive'
    elif N == 0:
        ans = 'zero'
    else:
        ans = 'negative'
    return ans

ans_list = [solve(3),solve(-1),solve(0),solve(1),solve(-13)]

for i in ans_list:
    print(i)
