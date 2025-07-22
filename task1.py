'''Day 1: Minimum Operations to Reduce X to Zero
🧞‍♂️
easy
You are given an integer array a of length n and an integer x.

In one operation, you can remove the leftmost or rightmost element from the array. The value of the removed element is then subtracted from 
.

Your goal is to perform a minimum number of such operations so that 
 becomes exactly 
. If it's not possible, print 
.

Note: The removed elements no longer appear in the array for future operations.
Input Format:
The first line contains two integers 
 and 
 (
, 
) --- the size of the array and the target value.

The second line contains 
 integers 
 (
) --- the elements of the array.
Output Format:
Print a single integer --- the minimum number of operations to make 
 exactly zero, or 
 if it is not possible.
Examples:
Example 1:
Input:

5 5
1 1 4 2 3

Output:

2
'''

def funct(n, x, a):
    total = sum(a)
    target = total - x

    if target < 0:
        return -1
    if target == 0:
        return n 

    max_len = -1
    curr_sum = 0
    left = 0

    for right in range(n):
        curr_sum += a[right]

        while curr_sum > target and left <= right:
            curr_sum -= a[left]
            left += 1

        if curr_sum == target:
            max_len = max(max_len, right - left + 1)

    return n - max_len if max_len != -1 else -1

n, x = map(int, input().split())
a = list(map(int, input().split()))
print(funct(n, x, a))
