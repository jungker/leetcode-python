class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        size = len(s)
        i, j = 0, size - 1
        while i <= j:
            if s[i].isalnum() and s[j].isalnum() and s[i].lower() == s[j].lower():
                i += 1
                j -= 1
            elif not s[i].isalnum():
                i += 1
            elif not s[j].isalnum():
                j -= 1
            else:
                return False
        return True


if __name__ == '__main__':
    s = "A man, a plan, a canal: Panama"
    # s = 'race a car'
    # s = '.,'
    solution = Solution()
    print solution.isPalindrome(s)
