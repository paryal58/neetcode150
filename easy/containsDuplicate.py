"""
Contains Duplicate

Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

Example 1:
Input: nums = [1, 2, 3, 3]
Output: true

Example 2:
Input: nums = [1, 2, 3, 4]
Output: false
"""

"""
Solution Logic:

Hash Sets has certain properties that allow us to solve this problem easily.
- They store only unique elements (If an element already in set is inserted again, it simply ignores that insertion)
- Meanwhile arrays can have duplicate elements

So, to check if the array has duplicate items or not, we simply can insert all items in array to the set
And then we can compare if the length of them are different.
Different length -> there is duplicate
Same length -> there is no duplicate and all are unique

"""

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Make set of all items in list
        mySet = set(nums)

        # Check if length are different or not
        return len(mySet) != len(nums)