# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

 
# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]


class Solution(object):
    def twoSum(self, nums, target):
        prevMap = {}

        for i, num in enumerate(nums):
            match = target - num
            if match in prevMap:
                return [prevMap[match], i]
            else:
                prevMap[num] = i

# Time Complexity: O(n)
    # O(n) where n is the number of elements in the 'nums' array
            # we iterate over the array exactly once using a single loop
            # each dictionary operation(checking if an element exists and adding amd element) is O(1) on average
# Space Complexity: O(n)
    # O(n) where n is the number of elements in the 'nums' array
            # this is because at worst case, we might store all the elements of the array in the dictionary 'prevMap'
