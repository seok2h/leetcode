"""
21. Merge Two Sorted Lists
url: https://leetcode.com/problems/merge-two-sorted-lists/

You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.
"""

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()

        if list1.val < list2.val:
            head.val = list1.val
            list1 = list1.next
        else:
            head.val = list2.val
            list2 = list2.next

        currentNode = head


        while list1 != None and list2 != None:
            currentNode.next = ListNode()
            currentNode = currentNode.next
            if list1.val < list2.val:
                 currentNode.val = list1.val
                 list1 = list1.next
            else:
                currentNode.val = list2.val
                list2 = list2.next

        while list1 != None:
            currentNode.next = ListNode()
            currentNode =currentNode.next
            currentNode.val = list1.val
            list1 = list1.next

        while list2 != None:
            currentNode.next = ListNode()
            currentNode = currentNode.next
            currentNode.val = list2.val
            list2 = list2.next

        return head



