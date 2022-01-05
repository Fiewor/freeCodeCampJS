function sumPrimes(num) {
let sieve = [], primes = []
for(let i = 2; i <= num; ++i){
  if(!sieve[i]){
    primes.push(i)
  }
  for(let j = i << 1; j <= num; j += i){
    sieve[j] = true
  }
}
return primes
.reduce((a,b)=>a+b)
}

console.log(sumPrimes(10))