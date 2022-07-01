function findAverage (k, array) {
  const result = []

  let windowSum = 0
  let windowStart = 0

  for (let windowEnd = 0; windowEnd < array.length; windowEnd++) {
    windowSum += array[windowEnd]

    if (windowEnd >= k - 1) {
      result.push(windowSum / k)
      windowSum = windowSum - array[windowStart]
      windowStart++
    }
  }
  return result
}

console.log(findAverage(5, [1, 3, 2, 6, -1, 4, 1, 8, 2]))
