def solution(n, k):
    answer = []
    lst = list(range(1, n+1))
    dp = [0] * (n+1)
    dp[0], dp[1] = 1, 1
    for i in range(2, n+1):
        dp[i] = dp[i-1] * i
    
    val = (k-1) // dp[n-1]
    
    answer.append(lst[val])
    lst.remove(lst[val])
    k = (k-1) % dp[n-1]
    n-=1
    
    while n:
        val = k // dp[n-1]
        answer.append(lst[val])
        lst.remove(lst[val])
        k = k % dp[n-1]
        n -= 1
        
    return answer