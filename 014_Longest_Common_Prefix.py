from functools import reduce

class Solution:
    def LongestCommonPrefix(strs):
        if len(strs) == 0:
            return ""

        def TwoCommonPrefix(str1, str2):
            common_str = ""
            min_len = min(len(str1), len(str2))
            for i in range(0, min_len):
                if str1[i] != str2[i]:
                    break
                common_str += str1[i]
            return common_str
        
        return reduce(TwoCommonPrefix, strs)

if __name__ == "__main__":
    result1 = Solution.LongestCommonPrefix([])
    result2 = Solution.LongestCommonPrefix(['abc'])
    result3 = Solution.LongestCommonPrefix(['abc', 'ab', 'a'])
    print(result1, result2, result3)