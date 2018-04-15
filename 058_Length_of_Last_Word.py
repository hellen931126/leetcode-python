class Solution:
    def lengthOfLastWord(s):
        s = s.strip()
        l = s.split()
        if len(s) == 0 or s == False:
            return 0
        return len(l[-1])

if __name__ == "__main__":
    result1 = Solution.lengthOfLastWord("Hello World")
    result2 = Solution.lengthOfLastWord(" ")
    result3 = Solution.lengthOfLastWord("   ")
    result4 = Solution.lengthOfLastWord("")
    result5 = Solution.lengthOfLastWord("I like eating apple")
    print(result1, result2, result3, result4, result5)
        