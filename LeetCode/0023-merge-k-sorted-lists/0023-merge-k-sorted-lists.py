# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists or len(lists) == 0:
            return None
        while len(lists) > 1:
            mergedlists = []
            for i in range(0,len(lists),2):
                l1 = lists[i]
                l2 = lists[i+1] if (i+1) < len(lists) else None
                mergedlists.append(self.merge(l1,l2))
            lists = mergedlists
        return lists[0]
    def merge(self, l1,l2):
        dummy = ListNode()
        head = dummy
        while l1 and l2:
            if l1.val < l2.val:
                head.next = l1
                l1=l1.next
            else:
                head.next =l2
                l2 =l2.next
            head=head.next
        if l1:
            head.next =l1
        if l2:
            head.next = l2
        return dummy.next


 