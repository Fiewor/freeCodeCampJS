function pairElement(str) {
  let arr = [], next
  for(let i = 0; i < str.length; i++){
    switch(str[i]){
      case "G":
      next = "C"
      break
      case "C":
      next = "G"
      break
      case "A":
      next = "T"
      break
      case "T":
      next = "A"
      break
      default:
      next = null
      brea
    }
    arr.push([str[i], next])
  }
  return arr
}

console.log(pairElement("GCG"))