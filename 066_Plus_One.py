class Solution:
    def plusOne(digits):
        for i in range(1,len(digits) + 1):
            digits[-i] += 1
            if digits[-i] >= 10:
                digits[-i] %= 10
                continue
            return digits
        a = [1]
        a.extend(digits)
        return a

if __name__ == "__main__":
    result1 = Solution.plusOne([0])
    result2 = Solution.plusOne([9])
    result3 = Solution.plusOne([1,2,4])
    print(result1, result2, result3)