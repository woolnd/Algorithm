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
    func reverseKGroup(_ head: ListNode?, _ k: Int) -> ListNode? {
        let dummy = ListNode(-1)
        dummy.next = head
        var groupPrev = dummy
        
        while true {
            guard let kthNode = getKthNode(from: groupPrev, k: k) else {
                break
            }
            
            let groupNext = kthNode.next
            
            var prev = kthNode.next 
            var curr = groupPrev.next
        
            for _ in 0..<k {
                let nextTmp = curr?.next
                curr?.next = prev
                prev = curr
                curr = nextTmp
            }
            
            let tmp = groupPrev.next
            groupPrev.next = kthNode
            groupPrev = tmp!
        }
        
        return dummy.next
    }
    
    private func getKthNode(from node: ListNode, k: Int) -> ListNode? {
        var curr: ListNode? = node
        for _ in 0..<k {
            curr = curr?.next
            if curr == nil { return nil }
        }
        return curr
    }
}