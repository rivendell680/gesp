#!/usr/bin/env python3
import sys


def feasible(target: int, desserts, m: int, budget: int) -> bool:
    """Check whether we can buy m desserts with median sweetness >= target."""
    need_high = (m + 1) // 2

    high_costs = []
    low_costs = []
    for sweet, cost in desserts:
        if sweet >= target:
            high_costs.append(cost)
        else:
            low_costs.append(cost)

    if len(high_costs) < need_high:
        return False

    high_costs.sort()
    low_costs.sort()

    total = sum(high_costs[:need_high])
    remain = m - need_high

    i = need_high
    j = 0
    while remain > 0:
        pick_high = i < len(high_costs)
        pick_low = j < len(low_costs)
        if not pick_high and not pick_low:
            return False
        if pick_high and (not pick_low or high_costs[i] <= low_costs[j]):
            total += high_costs[i]
            i += 1
        else:
            total += low_costs[j]
            j += 1
        if total > budget:
            return False
        remain -= 1

    return total <= budget


def main() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return

    it = iter(data)
    budget = int(next(it))
    n = int(next(it))
    m = int(next(it))

    desserts = [(int(next(it)), int(next(it))) for _ in range(n)]
    desserts.sort(key=lambda x: x[0])

    sweets = sorted({sweet for sweet, _ in desserts})

    left, right = 0, len(sweets) - 1
    ans = sweets[0]

    while left <= right:
        mid = (left + right) // 2
        target = sweets[mid]
        if feasible(target, desserts, m, budget):
            ans = target
            left = mid + 1
        else:
            right = mid - 1

    print(ans)


if __name__ == "__main__":
    main()
