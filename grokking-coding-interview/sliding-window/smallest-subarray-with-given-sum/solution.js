
function smallestSubarrayGivenSum (s, array) {
  let windowStart = 0
  let windowSum = 0

  let minimumWindowSize = Infinity

  for (let windowEnd = 0; windowEnd < array.length; windowEnd++) {
    windowSum += array[windowEnd]

    while (windowSum >= s) {
      minimumWindowSize = Math.min(minimumWindowSize, windowEnd - windowStart + 1)
      windowSum -= array[windowStart]
      windowStart += 1
    }
  }

  return minimumWindowSize
}

console.log(smallestSubarrayGivenSum(7, [2, 1, 5, 2, 3, 2]))
console.log(smallestSubarrayGivenSum(7, [2, 1, 5, 2, 8]))
console.log(smallestSubarrayGivenSum(8, [3, 4, 1, 1, 6]))
