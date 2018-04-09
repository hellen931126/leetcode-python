class Solution:
    def isValid(s):
        d = {")":"(", "]":"[", "}":"{"}
        stack = []
        for i in s:
            if i in d.values():
                stack.append(i)
            elif i in d.keys():
                if stack == [] or d[i] != stack.pop():
                    return False
            else:
                return False
        return stack == []

if __name__ == "__main__":
    result1 = Solution.isValid("")
    result2 = Solution.isValid("[")
    result3 = Solution.isValid("{}()")
    result4 = Solution.isValid("({})")
    result5 = Solution.isValid("()[")
    print(result1, result2, result3, result4, result5)