class Solution:
    def CountAndSay(n):
        s = '1'
        for _ in range(n-1):
            start, temp, count = s[0], '', 0
            for l in s:
                if start == l:
                    count += 1
                else:
                    temp += str(count) + start
                    start = l
                    count = 1
            temp += str(count) + start
            s = temp
        return s

if __name__ == "__main__":
    result1 = Solution.CountAndSay(1)
    result2 = Solution.CountAndSay(2)
    result3 = Solution.CountAndSay(3)
    result4 = Solution.CountAndSay(4)
    result5 = Solution.CountAndSay(5)
    print(result1, result2, result3, result4, result5)
