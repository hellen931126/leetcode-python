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
    def deleteDuplicates(head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        cur = head
        while cur:
            while cur.next and cur.next.val == cur.val:
                cur.next = cur.next.next
            cur = cur.next
        return head

if __name__ == "__main__":
    ListNode_1, ListNode_2 = ListNode_handle(), ListNode_handle()
    l1, l2 = ListNode(0), ListNode(0)
    l1_list, l2_list = [2,1,1], [3,3,2,1,1]
    for i in l1_list:
        l1 = ListNode_1.add(i)
    # l1 : 1 --> 1 --> 2
    for j in l2_list:
        l2 = ListNode_2.add(j)
    # l2 : 1 --> 1 --> 2 --> 3 --> 3

    result1 = Solution.deleteDuplicates(l1)
    # result1: 1 --> 2 
    result1List = [result1.val]
    while result1.next:
        result1 = result1.next
        result1List.append(result1.val)  
    print(result1List) 

    result2 = Solution.deleteDuplicates(l2)
    # result2: 1 --> 2 --> 3
    result2List = [result2.val]
    while result2.next:
        result2 = result2.next
        result2List.append(result2.val)  
    print(result2List)    


