import math

def gcd_exclusion(n, q, arr, queries):
    prefix_gcd = [0] * n
    suffix_gcd = [0] * n

    # ---> Build prefix GCD
    prefix_gcd[0] = arr[0]
    for i in range(1, n):
        prefix_gcd[i] = math.gcd(prefix_gcd[i-1], arr[i])

    # ---> Build suffix GCD
    suffix_gcd[-1] = arr[-1]
    for i in range(n-2, -1, -1):
        suffix_gcd[i] = math.gcd(suffix_gcd[i+1], arr[i])

    # ---> Process each query
    results = []
    for l, r in queries:
        l -= 1  # Convert to 0-based
        r -= 1
        if l == 0:
            results.append(suffix_gcd[r+1])
        elif r == n-1:
            results.append(prefix_gcd[l-1])
        else:
            results.append(math.gcd(prefix_gcd[l-1], suffix_gcd[r+1]))

    return results

# Input Reading
n, q = map(int, input().split())
arr = list(map(int, input().split()))
queries = [tuple(map(int, input().split())) for _ in range(q)]

# Output
answers = gcd_exclusion(n, q, arr, queries)
for ans in answers:
    print(ans)
