def solve(X,Y):
    
    if X>0 and Y>0:
        res = 1
    elif X<0 and Y>0:
        res = 2
    elif X<0 and Y<0:
        res = 3
    else:
        res = 4

    return res

print(solve(1,2),solve(-1,-3),solve(-2,1),solve(-3,-2),solve(2,-1), sep='\n')