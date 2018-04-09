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
    def mergeTwoLists(l1, l2):
        dummy = cur = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        cur.next = l1 or l2
        return dummy.next

if __name__ == "__main__":
    ListNode_1, ListNode_2 = ListNode_handle(), ListNode_handle()
    l1, l2 = ListNode(0), ListNode(0)
    l1_list, l2_list = [4,2,1], [4,3,1]
    for i in l1_list:
        l1 = ListNode_1.add(i)
    # l1 : 1 --> 2 --> 4
    for j in l2_list:
        l2 = ListNode_2.add(j)
    # l2 : 1 --> 3 --> 4

    result = Solution.mergeTwoLists(l1, l2)
    # result: 1 --> 1 --> 2 --> 3 --> 4 --> 4
    resultList = [result.val]
    while result.next:
        result = result.next
        resultList.append(result.val)  
    print(resultList)
    #[1,1,2,3,4,4]
    


