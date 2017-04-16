class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        size = len(height)
        if not size:
            return 0
        leftMax = [0 for i in range(size)]
        rightMax = [0 for i in range(size)]
        for i in range(1, size):
            leftMax[i] = max(leftMax[i - 1], height[i - 1])
            rightMax[size - i - 1] = max(rightMax[size - i], height[size - i])
        res = 0
        for i in range(1, size - 1):
            t = min(leftMax[i], rightMax[i])
            if t > height[i]:
                res += (t - height[i])
        return res


if __name__ == '__main__':
    x = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    solution = Solution()
    print solution.trap(x)
