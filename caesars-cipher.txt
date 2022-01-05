function rot13(str) {
  let arr = [], curr
  let punc= /[^A-Z]+/g
  for(let i = 0; i < str.length; i++){
    curr = str.charCodeAt(i)
    if(!punc.test(str[i])){
      curr <= 77
      ? curr+=13
      : curr-=13
    }
    arr.push(curr)
  }
  return arr
  .map(
    a=>String.fromCharCode(a)
  )
  .join("")
  //return String.fromCharCode(arr)
}

console.log(
rot13("SERR PBQR PNZC")
)