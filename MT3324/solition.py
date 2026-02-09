#!/usr/bin/env python3
import sys

def main() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    arr = [int(next(it)) for _ in range(n)]

    total = 0
    prev = {}
    for x in arr:
        cur = {x: 1}
        for val, cnt in prev.items():
            new_val = val & x
            cur[new_val] = cur.get(new_val, 0) + cnt
        for val, cnt in cur.items():
            total += val * cnt
        prev = cur

    print(total)

if __name__ == "__main__":
    main()
