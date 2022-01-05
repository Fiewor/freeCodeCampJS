function myReplace(str, before, after) {
  let first, rest
  if (before[0] === before[0].toUpperCase()){
  first = after[0].toUpperCase()
rest = after.slice(1, after.length)
after = first + rest
  }else{
    first = after[0].toLowerCase()
    rest = after.slice(1, after.length)
    after = first + rest
  }
  return str.replace(before, after);
}
console.log(myReplace("His name is Tom", "Tom", "john"))