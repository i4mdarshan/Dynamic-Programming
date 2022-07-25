n = int(input())


def fibonacciNumber(n, memo={}):
    MOD = 1000000007
    if n in memo:
        return memo[n] % MOD
    if n <= 2:
        return 1
    memo[n] = fibonacciNumber(n-1, memo) + fibonacciNumber(n-2, memo)
    return memo[n] % MOD
