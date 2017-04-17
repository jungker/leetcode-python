class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        t = 0
        for i in nums:
            t ^= i
        return t


if __name__ == '__main__':
    x = [2, 2, 2, 3, 2]
    solution = Solution()
    print solution.singleNumber(x)
