class Solution:
    def isPalindrome(x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        x = str(x)
        for i in range(0, len(x)//2):
            if x[i] != x[-(i+1)]:
                return False
        return True

if __name__ == "__main__":
    result1 = Solution.isPalindrome(-10)
    result2 = Solution.isPalindrome(10)
    result3 = Solution.isPalindrome(11)
    result4 = Solution.isPalindrome(121)
    result5 = Solution.isPalindrome(1000021)
    print(result1, result2, result3, result4, result5)