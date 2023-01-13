// https://leetcode.com/problems/number-of-nodes-in-the-sub-tree-with-the-same-label/

var countSubTrees = function (n, edges, labels) {
  const adj = {};
  for (let i = 0; i < n; i++) {
    adj[i] = [];
  }
  for (const edge of edges) {
    adj[edge[0]].push(edge[1]);
    adj[edge[1]].push(edge[0]);
  }

  let ans = Array(n);
  dfs(0, -1, adj, labels, ans);
  return ans;
};
const dfs = (node, parent, adj, labels, ans) => {
  // store count of all alphabets in subtree of the node
  const nodeCounts = Array(26).fill(0);
  nodeCounts[labels[node] - "a"] = 1; // set count of current node to 1
  if (!adj[node]) return nodeCounts; // node has no neighbours
  //   else, node has children
  for (const child of adj[node]) {
    if (child === parent) continue;
    // recursive call with child as node and parent as node
    const childCounts = dfs(child, node, adj, labels, ans);
    // add frequencies of child node in parent node's frequency
    for (let i = 0; i < 26; i++) {
      nodeCounts[i] += childCounts[i];
    }
  }
  ans[node] = ++nodeCounts[labels.charCodeAt(node) - "a".charCodeAt(0)];
  return nodeCounts;
};
let n = 7,
  edges = [
    [0, 1],
    [0, 2],
    [1, 4],
    [1, 5],
    [2, 3],
    [2, 6],
  ],
  labels = "abaedcd";
console.log(countSubTrees(n, edges, labels));
