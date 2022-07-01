function findAverage (k, array) {
  const answer = []
  for (let i = 0; i < array.length - k + 1; i++) {
    let sum = 0
    for (let j = i; j < i + k; j++) {
      sum += array[j]
    }
    answer.push(sum / k)
  }
  return answer
}

console.log(findAverage(5, [1, 3, 2, 6, -1, 4, 1, 8, 2]))
