function uniteUnique(...arr) {
  let neww = []
  for(let e of arr){
    for(let a of e){
      !neww.includes(a)
      && neww.push(a)
    }
  }
  return neww
}

console.log(uniteUnique([1, 3, 2], [5, 2, 1, 4], [2, 1]))