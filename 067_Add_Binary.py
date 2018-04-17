class Solution:
    def addBinary(a, b):
        length = 0
        dif = 0
        a, b = list(a) , list(b)
        if len(a) == len(b):
            length = len(a)
        if len(a) > len(b):
            length = len(a)
            dif = len(a) - len(b)
            for _ in range(dif):
                b.insert(0, "0")
        if len(b) > len(a):
            length = len(b)
            dif = len(b) - len(a)
            for _ in range(dif):
                a.insert(0, "0")
        carry = 0
        a = [int(x) for x in a]
        b = [int(x) for x in b]
        new_list = [0]*(length+1)
        for i in range(length-1, -1, -1):
            new_list[i+1] = a[i] + b[i] + new_list[i+1]
            if new_list[i+1] >= 2:
                new_list[i+1] = new_list[i+1] % 2
                new_list[i] += 1
        new_list = [str(x) for x in new_list]
        new_list = str(int("".join(new_list)))
        return new_list

if __name__ == "__main__":
    result1 = Solution.addBinary("1010", "1011")
    result2 = Solution.addBinary("0", "1")
    result3 = Solution.addBinary("1", "0")
    result4 = Solution.addBinary("11", "1")
    print(result1, result2, result3, result4)
            
            
            
            
            
        
        
            
        
        
            
        