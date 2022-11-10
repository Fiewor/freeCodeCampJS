var preorder = function (root) {
  if (!root) return [];
  let order = [],
    stack = [];
  stack.push(root);

  while (stack.length) {
    let node = stack.pop(),
      children = node.children;
    order.push(node.val);

    for (let i = children.length - 1; i >= 0; i--) {
      stack.push(node.children[i]);
    }
  }

  return order;
};
