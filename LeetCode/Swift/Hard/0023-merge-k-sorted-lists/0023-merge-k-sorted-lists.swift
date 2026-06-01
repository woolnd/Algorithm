/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public var val: Int
 *     public var next: ListNode?
 *     public init() { self.val = 0; self.next = nil; }
 *     public init(_ val: Int) { self.val = val; self.next = nil; }
 *     public init(_ val: Int, _ next: ListNode?) { self.val = val; self.next = next; }
 * }
 */
class Solution {
    func mergeKLists(_ lists: [ListNode?]) -> ListNode? {
        if lists.isEmpty { return nil }

        var currentLists = lists

        while currentLists.count > 1{
            var mergedLists: [ListNode?] = []
            var i = 0

            while i < currentLists.count {
                let l1 = currentLists[i]
                let l2 = (i + 1 < currentLists.count) ? currentLists[i + 1] : nil
                
                mergedLists.append(mergeTwoLists(l1, l2))
                i += 2 
            }
            
            currentLists = mergedLists
        }

        return currentLists[0]
    }

    private func mergeTwoLists(_ list1: ListNode?, _ list2: ListNode?) -> ListNode? {
        let dummy = ListNode(-1)
        var current = dummy
        var l1 = list1
        var l2 = list2

        while let n1 = l1, let n2 = l2 {
            if n1.val <= n2.val {
                current.next = n1
                l1 = n1.next
            } else {
                current.next = n2
                l2 = n2.next
            }

            current = current.next!
        }

        current.next = (l1 != nil) ? l1 : l2
        return dummy.next
    
    }
}