class Solution:
    def searchInsert(nums, target):
        for i in nums:
            if i == target:
                return nums.index(i)
        if target < nums[0]:
            return 0
        if target > nums[-1]:
            return len(nums)
        for j in range(len(nums)):
            if target > nums[j] and target < nums[j+1]:
                return nums.index(nums[j+1])

if __name__ == "__main__":
    result1 = Solution.searchInsert([1,3,5,6], 5)
    result2 = Solution.searchInsert([1,3,5,6], 2)
    result3 = Solution.searchInsert([1,3,5,6], 7)
    result4 = Solution.searchInsert([1,3,5,6], 0)
    print(result1, result2, result3, result4)