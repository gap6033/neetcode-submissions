# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def __init__(self):
        self.new_head = None
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        prev_node = None
        curr_node = head
        self.reverse(curr_node, curr_node.next)
        curr_node.next = prev_node
        return self.new_head


    def reverse(self, prev_node, curr_node):
        if not curr_node:
            self.new_head = prev_node
            return
        self.reverse(curr_node, curr_node.next)
        curr_node.next = prev_node
        return prev_node

'''
0
'''
        