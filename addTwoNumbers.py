# Solution for Add Two Numbers on Leetcode.

# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.



# Optimized Solution with Time = O(m,n) & space = O(m,n)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        l3 = ListNode(0)
        root = l3
        carry = 0
        
        while l1 != None or l2 != None or carry != 0:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            
            val = v1 + v2 + carry
            carry = val//10
            val = val%10
            
            l3.next = ListNode(val)
            
            l3 = l3.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            
            
        return root.next
            