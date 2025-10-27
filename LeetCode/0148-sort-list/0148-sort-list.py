# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        if not head or not head.next:
            return head

        def mid(head):
            slow, fast = head, head
            prev = None
            while fast and fast.next:
                prev = slow
                slow = slow.next
                fast = fast.next.next
            if prev:
                prev.next = None
            return slow
        
        def mergeSort(l1, l2):
            sorted_list = ListNode(-1)
            temp = sorted_list
            while l1 and l2:
                if l1.val < l2.val:
                    temp.next = l1
                    l1 = l1.next
                else:
                    temp.next = l2
                    l2 = l2.next
                temp = temp.next
            
            if l2:
                temp.next = l2
            else:
                temp.next = l1
            
            return sorted_list.next

        middle = mid(head)
        left = head
        right = middle

        return mergeSort(self.sortList(left), self.sortList(right))