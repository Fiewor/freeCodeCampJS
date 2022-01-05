function palindrome(str) {
  str = str
  .replace(/[^a-zA-Z0-9]+/g,"")
  .toLowerCase()
  let rev = str
          .split("")
          .reverse()
          .join("")
  return str === rev
}

console.log(
palindrome("a man, a plan, a canal. Panama")
)