class Solution {
    func divide(_ dividend: Int, _ divisor: Int) -> Int {
        if divisor == 1 {
            return dividend
        }

        if divisor == -1 && dividend == Int32.min {
            return Int(Int32.max)
        }
        
        if divisor == -1 {
            return -dividend
        }

        let isNegative = (dividend < 0) != (divisor < 0)

        var absDividend = abs(dividend)
        let absDivisor = abs(divisor)

        var result = 0

        while absDividend >= absDivisor{
            var tempDivisor = absDivisor
            var multiple = 1

            while absDividend >= tempDivisor << 1 {
                tempDivisor <<= 1
                multiple <<= 1
            }

            absDividend -= tempDivisor
            result += multiple
        }

        return isNegative ? -result : result
    }
}