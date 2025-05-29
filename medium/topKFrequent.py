"""
Top K Frequent Elements

Given an integer array nums and an integer k, return the k most frequent elements within the array.
The test cases are generated such that the answer is always unique.
You may return the output in any order.

Example 1:
Input: nums = [1,2,2,3,3,3], k = 2
Output: [2,3]

Example 2:
Input: nums = [7,7], k = 1
Output: [7]
"""

"""
Solution Logic:

- Implement a hash map of item and their frequency
- Sort the map based on their frequencies
- Return the value of top k items
"""

class Solution:
    def topKFrequent(self, nums : List[int], k : int) -> List[int]:
        myMap = {}
        for num in nums:
            myMap[num] = myMap.get(num, 0) + 1
        # Sort the map based on frequencies
        myMap = dict(sorted(myMap.items(), key=lambda x:x[1], reverse=True))
        return list(myMap.values())[:k]