# 1番目の人の偏差値を算出
# 操作を細分化することを意識

# 感想
# 結構実装難易度高め？？
# numpyのやつを使えば簡単だけど、甘えずに実装頑張った

def mean(li,N):
    ans = sum(li)/N
    return ans

def st(li,me,N):
    pre = 0
    for i in li:
        pre += ((i-me)**2) /N
    ans = pre ** (1/2)
    return ans

# 生徒の人数
N = 5
# 試験の点数
scores = [70, 50, 85, 69, 63]

score_mean = mean(scores,N)
score_std  = st(scores,score_mean,N)
ans = 50 + ((scores[0]-score_mean)/score_std)*10
print(ans)
