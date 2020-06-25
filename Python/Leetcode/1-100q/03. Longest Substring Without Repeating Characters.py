'''
 * Question Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/
'''

class Solution:
    def lengthOfLongestSubstring(self, text: str) -> int:
        max_len, s, e = 0, 0, 0
        seen = set()
        while s < len(text) and e < len(text):
            if text[e] in seen:
                seen.remove(text[s])
                s += 1
            else:
                seen.add (text[e])
                max_len = max(max_len, e - s + 1)
                e += 1
        return max_len
    
    
