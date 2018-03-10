class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        for k1, v1 in enumerate(nums):                  
            for k2, v2 in enumerate(nums[(k1+1):]):
                if v1 + v2 == target:
                    return [k1, k2+k1]
        return []

            