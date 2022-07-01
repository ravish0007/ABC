
function longestStringAfterReplacement (k, string) {
  let windowStart = 0
  const charMap = new Map()
  let maxRepeatingCharCount = 0

  let longestStringCount = -Infinity

  for (let windowEnd = 0; windowEnd < string.length; windowEnd++) {
    const char = string[windowEnd]

    if (!charMap.has(char)) {
      charMap.set(char, 0)
    }
    charMap.set(char, charMap.get(char) + 1)

    maxRepeatingCharCount = Math.max(maxRepeatingCharCount, charMap.get(char))

    if ((windowEnd - windowStart + 1 - maxRepeatingCharCount) > k) {
      const char = string[windowStart]
      charMap.set(char, charMap.get(char) - 1)
      windowStart++
    }

    longestStringCount = Math.max(longestStringCount, windowEnd - windowStart + 1)
  }
  return longestStringCount
}

for (const [string, k] of [['aabccbb', 2], ['abbcd', 1], ['abccde', 1]]) {
  console.log(longestStringAfterReplacement(k, string))
}

// Input: String="aabccbb", k=2
// Output: 5

// Input: String="abbcb", k=1
// Output: 4
// Explanation: Replace the 'c' with 'b' to have a longest repeating substring "bbbb".
// Example 3:

// Input: String="abccde", k=1
// Output: 3
