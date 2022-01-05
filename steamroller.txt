function steamrollArray(arr) {
  return arr
  .reduce((a,b)=>a
    .concat(Array.isArray(b) ? steamrollArray(b): b), [])
}
console.log(
steamrollArray([1, [2], [3, [[4]]]])
)