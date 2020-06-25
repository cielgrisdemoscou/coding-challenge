'''
 * Question Link: https://leetcode.com/problems/plus-one/
'''

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = list(map(str, digits))
        nums = int(''.join(digits))
        nums += 1
        nums = list(str(nums))
        return list(map(int, nums))
