function translatePigLatin(str) {
  let con = /^[^aeiou]+/gi
  let vow = /[aeiou]+/gi
  if(con.test(str)){
    let iOfV = str.search(vow)
    if(iOfV !== -1){
     let rem = str.substring(0, iOfV)
     return str.slice(iOfV, str.length)
    + rem
    + "ay"
    }
    return str + "ay"
  }else{
    return str + "way"
  }
  //return str;
}

console.log(translatePigLatin("ckkkonsonant"))