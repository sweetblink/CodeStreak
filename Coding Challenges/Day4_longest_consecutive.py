# Day 4: Longest Consecutive Subsequence
# Problem Statement:
# Given an unsorted array of integers, find the length of the longest 
# consecutive elements sequence. The solution should run in O(n) time complexity.

# Input Format:
# - A single integer T representing the number of test cases.
# - Each of the next T test cases consists of:
#   - An integer N (size of the array).
#   - N space-separated integers representing the array elements.

# Output Format:
# For each test case, print a single integer representing 
# the length of the longest consecutive sequence.

# Constraints:
# 1 ≤ T ≤ 10
# 1 ≤ N ≤ 10^5
# -10^9 ≤ Array Elements ≤ 10^9

# Example Input:
# 2
# 6
# 100 4 200 1 3 2
# 7
# 10 20 30 40 50 60 70
#
# Example Output:
# 4
# 1

def longest_consecutive_sequence(arr):
    """Function to find the length of the longest consecutive sequence in an array."""
    num_set = set(arr)  # Convert array to set for O(1) lookup
    longest = 0

    for num in num_set:
        if num - 1 not in num_set:  # Start of a sequence
            length = 1
            while num + length in num_set:
                length += 1
            longest = max(longest, length)

    return longest

# Taking input
T = int(input())  # Number of test cases
for _ in range(T):
    N = int(input())  # Number of elements in the array
    arr = list(map(int, input().split()))  # Array elements
    print(longest_consecutive_sequence(arr))  # Output the result
