# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


def printRandomListNode(p):
    while p:
        print p.label,
        p = p.next
    print


class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        res = t = RandomListNode(0)
        p = head
        d = {}
        while p:
            t.next = RandomListNode(p.label)
            d[p] = t.next
            t = t.next
            p = p.next
        t = res.next
        p = head
        while p:
            if p.random:
                t.random = d[p.random]
            p = p.next
            t = t.next
        return res.next


if __name__ == '__main__':
    solution = Solution()
    a = head = RandomListNode(1)
    b = head.next = RandomListNode(2)
    c = head.next.next = RandomListNode(3)
    d = head.next.next.next = RandomListNode(4)
    b.random = a
    a.random = c
    printRandomListNode(head)
    res = solution.copyRandomList(head)
    printRandomListNode(res)
