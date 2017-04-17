# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def printListNode(p):
    while p:
        print p.val,
        p = p.next
    print


class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        res0 = res = ListNode(0)
        p, q = head, head.next
        while q:
            if p.val != q.val:
                res.next = p
                res = res.next
            else:
                while p.next and p.val == p.next.val:
                    p = p.next
            p = p.next if p else None
            q = p.next if p else None
        res.next = p
        return res0.next

if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(3)
    head.next.next.next.next = ListNode(4)
    head.next.next.next.next.next = ListNode(4)
    head.next.next.next.next.next.next = ListNode(5)
    solution = Solution()
    res = solution.deleteDuplicates(head)
    printListNode(res)
