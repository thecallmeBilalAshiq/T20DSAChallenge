import sys
input = sys.stdin.readline

def max_beauty_minus_distance(a):
    n = len(a)
    # L[j] = best (a[i] + i) for i<j
    L = [float('-inf')] * n
    best = a[0] + 0
    for j in range(1, n):
        L[j] = best
        val = a[j] + j
        if val > best:
            best = val

    # R[j] = best (a[k] - k) for k>j
    R = [float('-inf')] * n
    best = a[-1] - (n-1)
    for j in range(n-2, -1, -1):
        R[j] = best
        val = a[j] - j
        if val > best:
            best = val

    # Combine
    answer = float('-inf')
    for j in range(1, n-1):
        current = L[j] + a[j] + R[j]
        if current > answer:
            answer = current

    return answer

def main():
    n = int(input())
    a = list(map(int, input().split()))
    print(max_beauty_minus_distance(a))

if __name__ == "__main__":
    main()
