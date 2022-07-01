
function noRepeat (string) {
  let windowStart = 0
  const wordSet = new Map()
  let longestDistinctLength = -Infinity

  for (let windowEnd = 0; windowEnd < string.length; windowEnd++) {
    const char = string[windowEnd]

    while (wordSet.has(char)) {
      const beginingChar = string[windowStart]

      if (wordSet.get(beginingChar) > 1) {
        wordSet.set(beginingChar, wordSet.get(beginingChar) - 1)
      } else {
        wordSet.delete(beginingChar)
      }
      windowStart += 1
    }

    wordSet.set(char, 1)
    longestDistinctLength = Math.max(longestDistinctLength, windowEnd - windowStart + 1)
  }

  return longestDistinctLength
}

for (const string of ['aabccbb', 'abbbb', 'abccde']) { console.log(noRepeat(string)) }
