class Solution:
    def climbStairs(n):
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2

        two_way_before = 1
        one_way_before = 2
        all_ways = 0
        for i in range(2, n):
            all_ways = two_way_before + one_way_before
            two_way_before = one_way_before
            one_way_before = all_ways
        return all_ways

if __name__ == "__main__":
    result1 = Solution.climbStairs(0)
    result2 = Solution.climbStairs(3)
    result3 = Solution.climbStairs(4)
    result4 = Solution.climbStairs(5)
    print(result1, result2, result3, result4)
