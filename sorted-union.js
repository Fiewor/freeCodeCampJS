function uniteUnique(...arr) {
  let newA = [];
  for(let a of arr){
    for(e of a){
      !newA.includes(e) 
      && newA.push(e)
    }
  }
  return newA
}

console.log(uniteUnique([1, 3, 2], [5, 2, 1, 4], [2, 1]))