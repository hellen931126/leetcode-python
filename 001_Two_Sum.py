import time

# my first solution
class Solution:
    def twoSum(self, nums, target):
        for k1, v1 in enumerate(nums):                  
            for k2, v2 in enumerate(nums[(k1+1):]):
                if v1 + v2 == target:
                    return [k1, k2+k1+1]
        return []

# Below is another better solution on line, because it costs less time
class Solution2:
    def twoSum(self, nums, target):
        if len(nums) <= 1:
            return False
        buff_dict = {}
        for i in range(len(nums)):
            if nums[i] in buff_dict:
                return [buff_dict[nums[i]], i]
            else:
                buff_dict[target-nums[i]] = i


if __name__ == "__main__":
    nums = [2, 7, 11, 15, 0]
    target = 9
    before = time.time()
    print(Solution().twoSum(nums, target))
    print(time.time() - before)

    before2 = time.time()
    print(Solution2().twoSum(nums, target))
    print(time.time() - before2)
    

