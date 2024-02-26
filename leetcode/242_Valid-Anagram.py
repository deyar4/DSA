'''
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
 

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
 

Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?
'''


# Brute-force approach (since we sort it's O(nlogn)) | (Runtime: 63ms, 14.99%) | (Memory: 17.29MB, 57.24%)



class Solution1:
    def isAnagram(s: str, t: str) -> bool:
        word1 = ''.join(sorted(s))
        word2 = ''.join(sorted(t))

        if len(word1) != len(word2):
            return False
        elif word1 == word2:
            return True
        else:
            return False
        


# Using frequency counts (it's O(n)) | (Runtime: 43ms, 86.09%) | (Memory: 16.95MS, 79.55% )
from collections import Counter

class Solution2:
    def isAnagram(s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        word1 = Counter(s)
        word2 = Counter(t)

        return word1 == word2

            


print(Solution2.isAnagram("anagram","nagaram"))