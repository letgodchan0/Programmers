def solution(storey):
    if storey < 5:return storey
    elif storey <= 10:return 10 - storey + 1

    storey = list(map(int, str(storey)))[::-1]    
    n = len(storey)
    dp = [0] * n
    check = 10 - storey[0]
    
    if storey[0] == 5:
        dp[0] = 5
        if storey[1] > 4:
            storey[1] += 1
    elif storey[0] > check:
        dp[0] = check
        storey[1] = storey[1]+1
    else:
        dp[0] = storey[0]

    for i in range(1,n-1):
        a, b = storey[i], 10 - storey[i]
        if a > b:
            dp[i] = dp[i-1] + b
            storey[i+1] = storey[i+1]+1
        else:
            dp[i] = dp[i-1] + a
            
    dp[-1] = dp[-2] + min(storey[-1], 10 - storey[-1] + 1)

    return dp[-1]