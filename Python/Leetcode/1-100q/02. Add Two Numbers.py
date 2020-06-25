'''
 * Question Link: https://leetcode.com/problems/add-two-numbers/
'''

#Definition for singly-linked list.
class ListNode:
  def __init__(self, x):
    self.val = x
    self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        curn = l1
        num = 1
        first_number = 0
        while curn:
            first_number += curn.val * num
            curn = curn.next
            num *= 10
            
        curn = l2
        num = 1
        second_number = 0
        
        while curn:
            second_number += curn.val * num
            curn = curn.next
            num *= 10
            
        number = first_number + second_number
        
        head = None
        for i in reversed(str(number)):
            print(i)
            if not head:
                head = ListNode(int(i))
                curn = head
            else:
                curn.next = ListNode(int(i))
                curn = curn.next
        return head
