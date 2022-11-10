const makeNode = (value) => {
  return {
    value,
    next: null,
  };
};

class List {
  constructor() {
    this.head = null;
    this.tail = null;
    this.size = 0;
  }

  append(value) {
    let node = makeNode(value);
    if (!this.tail) {
      this.head = this.tail = node;
      return node;
    }
    this.tail.next = node;
    this.tail = node;

    return node;
  }

  prepend(value) {
    let node = makeNode(value);
    if (!this.head) {
      this.head = this.tail = node;
      return node;
    }
    node.next = this.head;
    this.head = node;

    return node;
  }

  print() {
    let current = this.head;
    while (current) {
      console.log(current);
      current = current.next;
    }
  }

  removeFirst() {
    if (!this.head) {
      return null;
    }

    let nodeToRemove = this.head;
    this.head = nodeToRemove.next;

    nodeToRemove.next = null;

    if (nodeToRemove === this.tail) {
      this.tail = null;
    }

    return nodeToRemove;
  }

  findNodeBefore(node) {
    if (!node) {
      return null;
    }
    if (node === this.head) {
      return null;
    }
    let current = this.head;
    while (current) {
      if (current.next === node) {
        return current.next;
      }
      current = node.next;
    }
    return null;
  }

  removeLast() {
    if (!this.tail) {
      return null;
    }

    let node = this.head;
    if (node.next === this.tail) {
      let nodeToRemove = node.next;
    } else {
      node = node.next;
    }
  }
}

c;

let list = new List();
list.append(2);
list.append(1);
list.print();
// list;
