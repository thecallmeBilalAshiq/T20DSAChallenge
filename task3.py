#!/usr/bin/env python3
import sys

def max_removed_potholes(n, s0, s1):
    # Convert to weights: w[r][i]=1 if s_r[i]=='X', else 0
    w0 = [1 if c == 'X' else 0 for c in s0]
    w1 = [1 if c == 'X' else 0 for c in s1]

    # 1) Best single‐segment on each road via Kadane’s algorithm
    def kadane(w):
        best_end = best_all = 0
        for x in w:
            best_end = max(best_end + x, x)
            best_all = max(best_all, best_end)
        return best_all

    best0 = kadane(w0)
    best1 = kadane(w1)

    # 2) Build prefix‐max arrays
    #    prefix0[i] = best subarray sum of w0 in [0..i]
    #    prefix1[i] = best subarray sum of w1 in [0..i]
    prefix0 = [0] * n
    prefix1 = [0] * n
    cur0 = cur1 = 0
    for i in range(n):
        cur0 = max(cur0 + w0[i], w0[i])
        prefix0[i] = cur0 if i == 0 else max(prefix0[i-1], cur0)
        cur1 = max(cur1 + w1[i], w1[i])
        prefix1[i] = cur1 if i == 0 else max(prefix1[i-1], cur1)

    # 3) Build suffix‐max arrays
    #    suffix0[i] = best subarray sum of w0 in [i..n-1]
    #    suffix1[i] = best subarray sum of w1 in [i..n-1]
    suffix0 = [0] * n
    suffix1 = [0] * n
    cur0 = cur1 = 0
    for i in range(n-1, -1, -1):
        cur0 = max(cur0 + w0[i], w0[i])
        suffix0[i] = cur0 if i == n-1 else max(suffix0[i+1], cur0)
        cur1 = max(cur1 + w1[i], w1[i])
        suffix1[i] = cur1 if i == n-1 else max(suffix1[i+1], cur1)

    # 4) Best “two‐segment” configuration
    #    We pick a gap column j (1 <= j <= n-2) where we switch roads,
    #    so we can have one segment entirely left of j on one road
    #    and one segment entirely right of j on the other.
    best_two = 0
    for j in range(1, n-1):
        # prefix on road0 + suffix on road1, or vice versa
        best_two = max(best_two,
                       prefix0[j-1] + suffix1[j+1],
                       prefix1[j-1] + suffix0[j+1])

    # Answer is the best of: do nothing (0), one‐segment on either road, or two‐segments
    return max(0, best0, best1, best_two)


def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    s0 = data[1].strip()
    s1 = data[2].strip()
    print(max_removed_potholes(n, s0, s1))


if __name__ == "__main__":
    main()
