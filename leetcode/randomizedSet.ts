// https://leetcode.com/problems/insert-delete-getrandom-o1/

class RandomizedSet {
  arr: number[];
  map: { [key: number]: number };
  constructor() {
    this.arr = [];
    this.map = {};
  }

  insert(val: number): boolean {
    if (this.arr.includes(val)) return false;

    this.arr.push(val);
    this.map[val] = this.arr.length - 1;
    return true;
  }

  remove(val: number): boolean {
    if (!this.arr.includes(val)) return false;

    // get last element
    let lastVal = this.arr[this.arr.length - 1];
    // get index of val
    let index = this.map[val];
    // put val at the end of array
    this.arr[this.arr.length - 1] = val;
    // put last val at index of val <- actually replace last element with val
    this.arr[index] = lastVal;
    // change index of lastVal to relfect change
    this.map[lastVal] = index;
    // remove last element in arr i.e. val
    this.arr.pop();
    // remove val from map
    delete this.map[val];
    return true;
  }

  getRandom(): number {
    return this.arr[Math.floor(Math.random() * this.arr.length)];
  }
}

// bunch of testcases
var obj = new RandomizedSet();
obj.insert(0);
obj.insert(1);
obj.remove(0);
obj.insert(2);
obj.remove(1);
var rand = obj.getRandom();
var insertAnother = obj.insert(2);
var rand1 = obj.getRandom();
// var param_1 = obj.insert(2);
// var param_1 = obj.insert(1);
// var param_1 = obj.insert(3);
// var param_2 = obj.remove(1);
// var param_3 = obj.getRandom();
