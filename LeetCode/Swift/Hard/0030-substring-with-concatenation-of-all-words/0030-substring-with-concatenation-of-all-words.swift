class Solution {
    func findSubstring(_ s: String, _ words: [String]) -> [Int] {
        if s.isEmpty || words.isEmpty { return [] }

        let sCount = s.count
        let wordLen = words[0].count
        let wordCount = words.count
        let window = wordLen * wordCount

        if sCount < window { return [] }

        var wordDict = [String: Int]()
        for word in words {
            wordDict[word, default: 0] += 1
        }

        var result = [Int]()
        let sArray = Array(s)

        for i in 0..<wordLen {
            var left = i
            var seenWords = [String: Int]()
            var wordsUsedCount = 0 
            
            for right in stride(from: i, to: sCount - wordLen + 1, by: wordLen) {
                let currentWord = String(sArray[right..<right + wordLen])
                
                if let count = wordDict[currentWord] {
                    seenWords[currentWord, default: 0] += 1
                    wordsUsedCount += 1
                    
                    while seenWords[currentWord]! > count {
                        let removedWord = String(sArray[left..<left + wordLen])
                        seenWords[removedWord]! -= 1
                        wordsUsedCount -= 1
                        left += wordLen 
                    }
                    
                    if wordsUsedCount == wordCount {
                        result.append(left)
                    }
                    
                } else {
                    seenWords.removeAll()
                    wordsUsedCount = 0
                    left = right + wordLen
                }
            }
        }

        return result
    }
}