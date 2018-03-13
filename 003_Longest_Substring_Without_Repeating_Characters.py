class Solution:
    def lengthOfLongestSubstring(self, s):
        maxLength = 0
        start = 0
        usedChar = {}

        for i in range(len(s)):
            if s[i] in usedChar and start <= usedChar[s[i]]:
                start = usedChar[s[i]] + 1
            else:
                maxLength = max(maxLength, i - start + 1)
            usedChar[s[i]] = i
        return maxLength

if __name__ == "__main__":
    s1 = "pwwkew"
    s2 = "abba"
    maxLength1 = Solution.lengthOfLongestSubstring(s1, s1)
    maxLength2 = Solution.lengthOfLongestSubstring(s2, s2)

    print(maxLength1, maxLength2)
