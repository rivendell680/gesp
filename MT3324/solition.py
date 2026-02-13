#!/usr/bin/env python3
import sys


def can_reach(target: int, items, budget: int, m: int) -> bool:
    need_high = (m + 1) // 2
    high = []
    low = []

    for sweet, price in items:
        if sweet >= target:
            high.append(price)
        else:
            low.append(price)

    if len(high) < need_high:
        return False

    high.sort()
    low.sort()

    total = sum(high[:need_high])
    if total > budget:
        return False

    rest = m - need_high
    i = 0
    j = need_high

    while rest > 0:
        low_price = low[i] if i < len(low) else None
        high_price = high[j] if j < len(high) else None

        if low_price is None and high_price is None:
            return False

        if high_price is None or (low_price is not None and low_price <= high_price):
            total += low_price
            i += 1
        else:
            total += high_price
            j += 1

        if total > budget:
            return False
        rest -= 1

    return total <= budget


def main() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return

    it = iter(data)
    budget = int(next(it))
    n = int(next(it))
    m = int(next(it))

    items = [(int(next(it)), int(next(it))) for _ in range(n)]
    sweets = sorted({s for s, _ in items})

    lo, hi = 0, len(sweets) - 1
    ans = sweets[0]

    while lo <= hi:
        mid = (lo + hi) // 2
        cand = sweets[mid]
        if can_reach(cand, items, budget, m):
            ans = cand
            lo = mid + 1
        else:
            hi = mid - 1

    print(ans)


if __name__ == "__main__":
    main()
