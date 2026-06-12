class Solution {
    func longestValidParentheses(_ s: String) -> Int {
        let chars = Array(s)
        var stack: [Int] = [-1] 
        var maxLength = 0
        
        for i in 0..<chars.count {
            if chars[i] == "(" {
                stack.append(i)
            } else {
                _ = stack.popLast()
                
                if stack.isEmpty {
                    stack.append(i)
                } else {
                    let currentLength = i - stack.last!
                    maxLength = max(maxLength, currentLength)
                }
            }
        }
        
        return maxLength
    }
}