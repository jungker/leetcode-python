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
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        res = ListNode(0)
        res.next = head
        p = head
        cnt = 0
        while p:
            p = p.next
            cnt += 1
        cnt /= k
        p, q = res, head
        for i in range(cnt):
            for j in range(k - 1):
                t = q.next
                q.next = t.next
                t.next = p.next
                p.next = t
            p = q
            q = p.next
        return res.next


if __name__ == '__main__':
    solution = Solution()
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    res = solution.reverseKGroup(head, 4)
    printListNode(res)
