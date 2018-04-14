class Solution:
    def maxSubArray(nums):
        
        if not nums:
            return 0

        curSum = maxSum = nums[0]
        for num in nums[1:]:
            curSum = max(num, curSum + num)
            maxSum = max(maxSum, curSum)

        return maxSum

if __name__ == "__main__":
    result1 = Solution.maxSubArray([])
    result2 = Solution.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
    print(result1, result2)