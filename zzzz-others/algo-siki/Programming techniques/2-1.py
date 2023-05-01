def solve(N):
    if N%3==0 and N%5==0:
        ans = 'FizzBuzz'
    elif N%3==0:
        ans = 'Fizz'
    elif N%5==0:
        ans = 'Buzz'
    else:
        ans = N
    
    print(ans)

for N in range(1,16):
    solve(N)
