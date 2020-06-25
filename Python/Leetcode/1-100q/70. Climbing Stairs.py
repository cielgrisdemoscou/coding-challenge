'''
 * Question Link: https://leetcode.com/problems/climbing-stairs/
'''

class Solution:
    def climbStairs(self, n: int) -> int:
        pre = cur = 1
        for i in range(1, n):
            pre, cur = cur, pre+cur
        return cur
