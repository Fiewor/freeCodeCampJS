function fearNotLetter(str) {
  let ar = [], miss
  for(let i = 0; i < str.length; i++){
    ar.push(str.charCodeAt(i))
  }
  for(let r = 0; r < ar.length; r++){
    (ar[r + 1] - ar[r]) > 1
    ? miss = ar[r] + 1
    // if i was to fill in the gap, i would use below
    // r.splice(ar[r], 0, ar[r] + 1) 
    : -1
  }
  return miss > 0
  ? String.fromCharCode(miss)
  : undefined
}
console.log(
  fearNotLetter("abce")
  )