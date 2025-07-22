'''


'''

def count_three_partitions(n, arr):
    MOD = 10**9 + 7  # ---> large output might be required modulo
    total = sum(arr)

    if total % 3 != 0:
        return 0

    target = total // 3
    prefix_sum = 0
    count_target = 0
    ways = 0

    # ---> Loop to n-1 to ensure last part is non-empty
    for i in range(n - 1):
        prefix_sum += arr[i]

        # ---> Check for 2*target second, so it doesn't interfere with target count
        if prefix_sum == 2 * target:
            ways = (ways + count_target) % MOD

        if prefix_sum == target:
            count_target += 1

    return ways


# ---> Input
n = int(input())
arr = list(map(int, input().split()))

# ---> Output
print(count_three_partitions(n, arr))
