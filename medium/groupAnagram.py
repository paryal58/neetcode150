"""
Group Anagrams
Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.
An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Example 1:
Input: strs = ["act","pots","tops","cat","stop","hat"]
Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]

Example 2:
Input: strs = ["x"]
Output: [["x"]]
"""

"""
Solution Logic:

Use defaultdict to form a map of anagramic sorted strings with list of anagrams
Steps:
- Initialize the map that can store list as its values
- Iterate through the list
    - Sort the string and make sorted strings the key
    - Append the current string to sorted string
        - If there is anagram the string gets appended to another else it forms new entry
- Return all values in the map
"""

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        myMap = defaultdict(list)
        for str in strs:
            myMap[''.join(sorted(str))].append(str)
        return myMap.values()