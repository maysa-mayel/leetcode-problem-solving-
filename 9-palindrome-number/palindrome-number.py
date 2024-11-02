class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        s =str(x)
        p = s[::-1]
        return s == p