    '''
 * Question Link: https://leetcode.com/problems/valid-parentheses/
'''

class Solution:
    def isValid(self, s: str) -> bool:
        match = {
        ')': '(',
        '}': '{',
        ']': '['
    }
        stack = []
        for c in s:
            if not stack:
                stack.append(c)
            else:
                if c not in match:
                    stack.append(c)
                else:
                    t = match[c]
                    if t != stack.pop():
                        return False
        return len(stack) == 0
        