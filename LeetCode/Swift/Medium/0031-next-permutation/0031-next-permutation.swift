class Solution {
    func nextPermutation(_ nums: inout [Int]) {
        var i = nums.count - 2

        while i >= 0 && nums[i] >= nums[i + 1] {
            i -= 1
        }

        if i >= 0 {
            for j in stride(from: nums.count - 1, through: i + 1, by: -1) {
                if nums[j] > nums[i] {
                    nums.swapAt(j, i)
                    break
                }
            }
        }

        var left = i + 1
        var right = nums.count - 1

        while left < right {
            nums.swapAt(left, right)
            left += 1
            right -= 1
        }
    }
}