##leetcode merging two lists problem 21

class ListNode(object):
    def mergeTwoLists(self, list1, list2):
        if list1 == None:
            return list2 
        elif list2 == None:
            return list1 
        dummyNode = ListNode(-1)
        tail = dummyNode 
        head = dummyNode 

        while list1 != None and list2 != None:
            if list1.val < list2.val:
                tail.next = list1 
                list1 = list1.next 
            else:
                tail.next = list2 
                list2 = list2.next 
            tail = tail.next

        if list1:
            tail.next = list1 
        else:
            tail.next = list2
        return head.next


###Leetcode 23
#Merge K sorted list

class Solution(object):
    def mergeKLists(self, lists):
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]
        # Split the list into two halves
        mid = len(lists) // 2
        l, r = self.mergeKLists(lists[:mid]), self.mergeKLists(lists[mid:])
        # Merge the two halves
        return self.merge(l, r)
    def merge(self, l, r):
        # Initialize a dummy node to help with merging
        dummy = p = ListNode()
        # Merge the two lists
        while l and r:
            if l.val < r.val:
                p.next = l
                l = l.next
            else:
                p.next = r
                r = r.next
            p = p.next
        # Attach the remaining elements, if any
        p.next = l or r
        # Return the merged list, which starts at dummy.next
        return dummy.next
    