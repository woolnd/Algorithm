class Solution {
    func isValid(_ s: String) -> Bool {
        let pairs: [Character : Character] = [ ")" : "(", "}" : "{", "]" : "["]

        var stack = [Character]()

        for char in s {
            if let requiredOpen = pairs[char] {
                if stack.isEmpty || stack.removeLast() != requiredOpen {
                    return false
                }
            } else {
                stack.append(char)
            }
        }

        if !stack.isEmpty {
            return false
        } else {
            return true
        }
    }
}