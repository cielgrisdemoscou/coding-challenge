'''
* Question Link: https://leetcode.com/problems/maximum-subarray/
'''

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr = 0
        Max = -10000000000
        
        for i in range( 0, len(nums) ):
            if curr < 0:
                curr = 0
            curr = curr + nums[ i ]
            Max = max( curr, Max )

        return Max
