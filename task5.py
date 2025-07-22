def max_dark_segment(n, p, lamps):
    MAX = 2 * 10**5 + 10
    diff = [0] * (MAX)

    for x, r in lamps:
        l = max(0, x - r)
        r = min(MAX - 2, x + r)
        diff[l] += 1
        diff[r + 1] -= 1

    coverage = [0] * (MAX)
    coverage[0] = diff[0]
    for i in range(1, MAX):
        coverage[i] = coverage[i - 1] + diff[i]

    max_dark = 0
    curr_dark = 0
    for i in range(0, p + 1):
        if coverage[i] != 1:
            curr_dark += 1
            max_dark = max(max_dark, curr_dark)
        else:
            curr_dark = 0

    return max_dark

# Example usage:
n, p = map(int, input().split())
lamps = [tuple(map(int, input().split())) for _ in range(n)]
print(max_dark_segment(n, p, lamps))
