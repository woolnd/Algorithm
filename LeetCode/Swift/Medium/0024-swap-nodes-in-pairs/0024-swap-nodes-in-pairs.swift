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
    func swapPairs(_ head: ListNode?) -> ListNode? {
        let dummy = ListNode(-1)
        dummy.next = head

        var prev = dummy
        
        while let node1 = prev.next, let node2 = node1.next {
            node1.next = node2.next
            node2.next = node1
            prev.next = node2

            prev = node1
        }

        return dummy.next
    }
}