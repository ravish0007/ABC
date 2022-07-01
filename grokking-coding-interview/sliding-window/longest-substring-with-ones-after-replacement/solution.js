
function longestOnes (k, string) {
  let windowStart = 0
  const charMap = new Map()
  let oneCount = 0
  let longestStringCount = -Infinity

  for (let windowEnd = 0; windowEnd < string.length; windowEnd++) {
    const char = string[windowEnd]

    if (char === 1) {
      oneCount += 1
    }

    if ((windowEnd - windowStart + 1 - oneCount) > k) {
      const char = string[windowStart]
      if (char === 1) {
        oneCount -= 1
      }
      windowStart++
    }

    longestStringCount = Math.max(longestStringCount, windowEnd - windowStart + 1)
  }
  return longestStringCount
}

console.log(longestOnes(2, [0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1]))
console.log(longestOnes(3, [0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1]))
