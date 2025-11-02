# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def modifiedList(self, nums, head):
        """
        :type nums: List[int]
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        cur = head
        dummy = ListNode(0)
        dummy.next= head
        prev = dummy
        list= set(nums)
        while cur:
            next= cur.next
            if cur.val in list:
                prev.next = next
            else:
                prev= cur
            cur=cur.next
        return dummy.next
