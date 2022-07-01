
function maximumSubarrayK (k, array) {
  let maximumSum = -Infinity
  let windowSum = 0
  let windowStart = 0

  for (let windowEnd = 0; windowEnd < array.length; windowEnd++) {
    windowSum += array[windowEnd]

    if (windowEnd >= k - 1) {
      if (maximumSum < windowSum) {
        maximumSum = windowSum
      }

      windowSum -= array[windowStart]
      windowStart += 1
    }
  }

  return maximumSum
}

console.log(maximumSubarrayK(3, [2, 1, 5, 1, 3, 2]))
