"""
Two Sum

Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.
You may assume that every input has exactly one pair of indices i and j that satisfy the condition.
Return the answer with the smaller index first.

Example 1:

Input: 
nums = [3,4,5,6], target = 7
Output: [0,1]

Explanation: nums[0] + nums[1] == 7, so we return [0, 1].

Example 2:
Input: nums = [4,5,6], target = 10
Output: [0,2]
"""

"""
Solution Logic:

Utilize dictionary to find solution. In first pass, insert all element to the set.
In the second pass, check if complement in the target.
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myDict = {}
        for i, num in enumerate(nums):
            myDict[num] = i
        for i, num in enumerate(nums):
            complement = target - num
            if complement in myDict and myDict[complement] != i:
                return [i, myDict[complement]]

        return False