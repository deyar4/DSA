'''
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

 

Example 1:

Input: nums = [1,2,3,1]
Output: true
Example 2:

Input: nums = [1,2,3,4]
Output: false
Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
 

Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109

'''

# Brute-Force Approach (488 ms - 15.97%)
class Solution1:
    def containsDuplicate(self, nums):
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return True
        return False

# Using sets for faster lookup (421 ms - 86.91%)
class Solution2:
    def containsDuplicate(self, nums):
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False 

# using counter (Better memory usage, slower runtime)
from collections import Counter

class Solution3:
    def containsDuplicate(self, nums):
        counts = Counter(nums)
        for count in counts.values():
            if count > 1:
                return True
            return False

# testing:
nums = [1, 2, 3, 1]
solution = Solution3()
print(solution.containsDuplicate(nums))

