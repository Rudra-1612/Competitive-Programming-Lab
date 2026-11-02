def fibonacci(n: int) -> int:
    """Return F(n), using bottom-up dynamic programming."""
    if n < 0:
        raise ValueError("n must be non-negative")
    if n <= 1:
        return n

    dp = [0] * (n + 1)
    dp[0], dp[1] = 0, 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


if __name__ == "__main__":
    n = 7
    print(f"F({n}) =", fibonacci(n))
