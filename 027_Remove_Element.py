class Solution:
    def removeElement(nums, val):
        while True:
            if val in nums:
                nums.pop(nums.index(val))
            else:
                break
        return len(nums)

if __name__ == "__main__":
    result1 = Solution.removeElement([3,2,2,3], 3)
    result2 = Solution.removeElement([1,2,1,5,1,3], 1)
    print(result1, result2)
    
