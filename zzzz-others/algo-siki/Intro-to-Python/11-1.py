# 標準入力から値を受け取る
# S: str 型
S = list(input())
consonant = ['a','i','u','e','o']

# 受け取った値を利用してコードを書いてください
for i in range(len(S)):
    
    # 母音ではない　かつ　小文字のものを置き換える
    if S[i] not in consonant and S[i].islower():
        S[i] = '_'

print(*S ,sep='')
