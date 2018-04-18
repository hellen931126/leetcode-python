import math

class Solution:
    def mySqrt(x):
        if x < 0:
            return 0
        return int(math.sqrt(x))

if __name__ == "__main__":
    result1 = Solution.mySqrt(9)
    result2 = Solution.mySqrt(5)
    print(result1, result2)