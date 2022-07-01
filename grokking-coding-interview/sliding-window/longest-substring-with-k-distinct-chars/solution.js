
function longestSubstringKdistinct (k, string) {
  const windowMap = new Map()
  let windowStart = 0

  let longestSubstringLength = -Infinity

  for (let windowEnd = 0; windowEnd < string.length; windowEnd++) {
    const char = string[windowEnd]

    if (!windowMap.has(char)) {
      windowMap.set(char, 0)
    }
    windowMap.set(char, windowMap.get(char) + 1)

    while (windowMap.size > k) {
      const char = string[windowStart]

      if (windowMap.get(char) == 1) {
        windowMap.delete(char)
      } else {
        windowMap.set(char, windowMap.get(char) - 1)
      }
      windowStart += 1
    }

    longestSubstringLength = Math.max(longestSubstringLength, windowEnd - windowStart + 1)
  }

  return longestSubstringLength
}

console.log(longestSubstringKdistinct(2, 'araaci'))
console.log(longestSubstringKdistinct(1, 'araaci'))
console.log(longestSubstringKdistinct(3, 'cbbebi'))
