#Definition for singly-linked list
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class ListNode_handle:
    def __init__(self):
        self.cur_node = None

    def add(self, data):
        #add a new node pointed to previous node
        node = ListNode(data)
        node.next = self.cur_node
        self.cur_node = node
        return node

    def print_ListNode(self, node):
        while node:
            print('\nvalue:', node.val)
            node = node.next

class Solution:
    def addTwoNumbers(l1, l2):
        dummy = cur = ListNode(0)
        carry = 0
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            cur.next = ListNode(carry%10)
            cur = cur.next
            carry //= 10
        return dummy.next

if __name__ == "__main__":
    ListNode_1, ListNode_2 = ListNode_handle(), ListNode_handle()
    l1, l2 = ListNode(0), ListNode(0)
    l1_list, l2_list = [3,4,2], [4,6,5]
    for i in l1_list:
        l1 = ListNode_1.add(i)
    # l1 : 2 --> 4 --> 3
    for j in l2_list:
        l2 = ListNode_2.add(j)
    # l2 : 5 --> 6 --> 4

    result = Solution.addTwoNumbers(l1, l2)
    # result: 7 --> 0 --> 8
    resultList = [result.val]
    while result.next:
        result = result.next
        resultList.append(result.val)  
    print(resultList)
    


