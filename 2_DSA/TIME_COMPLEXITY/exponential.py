#O(2ⁿ) — Exponential Time

def fibonacci_slow(n: int) -> int:
    # Each call spawns TWO more calls
    # This creates a binary tree of calls
    # Tree doubles in size with every increase in n
    # fib(5) → ~32 calls, fib(20) → ~1 million calls!

    if n <= 1:
        return n                                # Base case

    left_branch  = fibonacci_slow(n - 1)       # Branch 1 — spawns more calls
    right_branch = fibonacci_slow(n - 2)       # Branch 2 — spawns more calls

    return left_branch + right_branch

# ✅ Fixed version using memoization → brings it down to O(n)
from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci_fast(n: int) -> int:
    # lru_cache remembers already computed results
    # So each value is calculated only ONCE — no repeated branching
    if n <= 1:
        return n
    return fibonacci_fast(n - 1) + fibonacci_fast(n - 2)

print(fibonacci_slow(10))   # 55 — but took 177 function calls internally!
print(fibonacci_fast(10))   # 55 — took only 11 calls ✅
