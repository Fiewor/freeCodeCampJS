function smallestCommons(arr) {
  arr.sort((a,b)=>a-b)
  let count = 0, mult
  for(let i = arr[0]+1;
  i < arr[arr.length-1];
  i++
  ){
    arr
    .splice(1+count,0,i)
    count++
  }
  for(let j = 2;
  j < Number.POSITIVE_INFINITY;
  j++){
    mult = arr[0] * j
    if(arr
    .every(e=>mult%e===0)
    ) return mult
  }
}

console.log(smallestCommons([1,5]))