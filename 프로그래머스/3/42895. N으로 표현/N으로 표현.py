def solution(N, number):
    answer = 0
    dp = [set() for _ in range(9)]
    for t in range(1, 9):
        dp[t].add(int(str(N) * t))
        for i in range(1, t):
            for n in dp[i]:
                for m in dp[t-i]:
                    dp[t].add(n+m)
                    dp[t].add(n-m)
                    dp[t].add(n*m)
                    if n != 0 and m != 0:
                        dp[t].add(n//m)
        if number in dp[t]:
            return t
        
    return -1