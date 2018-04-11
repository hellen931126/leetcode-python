class Solution:
    def strStr(haystack, needle):
        if needle not in haystack:
            return -1
        return haystack.index(needle)

if __name__ == "__main__":
    result1 = Solution.strStr("hello", "ll")
    result2 = Solution.strStr("aaaaa", "bba")
    print(result1, result2)