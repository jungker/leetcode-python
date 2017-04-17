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
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        res = t = ListNode(0)
        if not head or not head.next:
            return head
        p, q = head, head.next
        while q:
            t1, t2 = p, q
            p = q.next
            q = p.next if p else None
            t.next = t2
            t = t.next
            t.next = t1
            t = t.next
        t.next = p
        return res.next


if __name__ == '__main__':
    solution = Solution()
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    # head.next.next.next = ListNode(4)
    res = solution.swapPairs(head)
    printListNode(res)
