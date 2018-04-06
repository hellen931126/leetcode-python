class Solution:
    def reverse(x):
        if x > 0: 
            s = 1
        if x == 0: 
            return 0
        if x < 0: 
            s = -1
        r = int(str(s*x)[::-1])
        return s*r * (r < 2**31)

if __name__ == "__main__":
    result1 = Solution.reverse(-123)
    result2 = Solution.reverse(123)
    result3 = Solution.reverse(120)
    print(result1, result2, result3)