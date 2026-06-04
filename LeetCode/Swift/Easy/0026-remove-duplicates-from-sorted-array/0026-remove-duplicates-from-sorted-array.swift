class Solution {
    func removeDuplicates(_ nums: inout [Int]) -> Int {
        if nums.isEmpty { return 0 }

        var insertIndex = 1
        
        for i in 1..<nums.count {
            if nums[i] != nums[i-1] {
                nums[insertIndex] = nums[i]

                insertIndex += 1
            }
        }

        return insertIndex
    }
}