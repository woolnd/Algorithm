class Solution {
    func removeElement(_ nums: inout [Int], _ val: Int) -> Int {
        var insertIndex = 0

        for i in 0..<nums.count {
            if nums[i] != val {
                nums[insertIndex] = nums[i]
                insertIndex += 1
            }
        }

        return insertIndex
    }
}