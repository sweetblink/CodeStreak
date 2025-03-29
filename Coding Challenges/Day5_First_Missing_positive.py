"""
🔹 Problem Statement: Find the First Missing Positive Integer

📝 Description:
Given an unsorted array of integers, find the smallest missing positive integer.

✅ Constraints:
1 ≤ T ≤ 10  (Number of test cases)
1 ≤ N ≤ 10⁵ (Size of the array)
-10⁶ ≤ nums[i] ≤ 10⁶ (Each element in the array)

🔍 Explanation:
- **Test Case 1:** The smallest missing positive integer is **2** because we have {1, 3, 4, 5}.
- **Test Case 2:** The smallest missing positive integer is **4** because {1, 2, 3} are present.

🎯 Expected Time Complexity: **O(N)** (Using Cyclic Sort)
"""

def first_missing_positive(nums):
    n = len(nums)
    
    # Step 1: Place each number at its correct index (Cyclic Sort)
    for i in range(n):
        while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
            nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
    
    # Step 2: Find the first missing number
    for i in range(n):
        if nums[i] != i + 1:
            return i + 1
    
    return n + 1  # If all are in place, return the next number

# Taking input
T = int(input())  # Number of test cases

for _ in range(T):
    N = int(input())  # Size of the array
    arr = list(map(int, input().split()))  # Read the array
    
    print(first_missing_positive(arr))  # Print the result
