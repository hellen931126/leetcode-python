class Solution:
    def removeDuplicates(nums):
        nums[:] = list(set(nums))
        nums.sort()
        return len(nums)

if __name__ == "__main__":
    result1 = Solution.removeDuplicates([1,1,2,1])
    print(result1)

   