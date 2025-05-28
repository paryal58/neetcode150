"""
Valid Anagram

Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.
An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Example 1:
Input: s = "racecar", t = "carrace"
Output: true

Example 2:
Input: s = "jar", t = "jam"
Output: false

Constraints:
s and t consist of lowercase English letters.
"""

"""
Solution Logic:

Dictionaries can be used to solve this problem. 
Store each character as key and their frequencies as values.
Use one string to populate and the other to depopulate and check if all final values are zero.

In example one, "racecar"
myMap[r] = 2, myMap[a] = 2, .... (Keys are the characters in the string and values are their frequencies)
Now using the string "carrace"
myMap[r] = 2-1-1 (Two occurance of r)
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Two words are not anagram if they are of different length 
        if len(s) != len(t):
            return False
        # Using dictionary 
        myMap = {}
        for ch in s:
            myMap[ch] = myMap.get(ch, 0) + 1
        for ch in t:
            if ch in myMap:
                myMap[ch] -= 1
            else:
                return False
        # Check if all values are 0
        for val in myMap.values():
            if val != 0:
                return False

        return True
