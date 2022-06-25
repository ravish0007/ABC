
const containsDuplicate = function (nums) {
  const sortedNums = nums.slice().sort()
  const prev = null

  for (const num of sortedNums) {
    if (num == prev) {
      return true
    }
    prev = num
  }

  return false
}
