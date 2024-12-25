function * enumerate (array) {
  let index = 0
  for (const element of array) {
    yield [index, element]
    index++
  }
}

const twoSum = function (nums, target) {
  const seen = new Map()
  for (const [index, num] of enumerate(nums)) {
    if (seen.has(target - num)) {
      return [seen.get(target - num), index]
    }
    seen.set(num, index)
  }
}
