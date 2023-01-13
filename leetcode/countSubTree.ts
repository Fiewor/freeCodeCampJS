// https://leetcode.com/problems/number-of-nodes-in-the-sub-tree-with-the-same-label/

export {}; // to remove TS error
function countSubTrees(n: number, edges: number[][], labels: string): number[] {
  const ans = Array();
  let adj = {};
  for (let i = 0; i < n; i++) {
    adj[i] = [];
  }
  for (const edge of edges) {
    adj[edge[0]].push(edge[1]);
    adj[edge[1]].push(edge[0]);
  }
  dfs(0, -1, adj, labels, ans);
  return ans;
}

const dfs = (
  node: number,
  parent: number,
  adj: {},
  labels: string,
  ans: number[]
) => {
  const nodeCounts = Array(26).fill(0);
  nodeCounts[+labels[node] - +"a"] = 1;
  if (!adj[node]) return nodeCounts;
  for (const child of adj[node]) {
    if (child !== parent) {
      const childCounts = dfs(child, node, adj, labels, ans);
      for (let i = 0; i < 26; i++) {
        nodeCounts[i] += childCounts[i];
      }
    }
  }
  ans[node] = ++nodeCounts[labels.charCodeAt(node) - "a".charCodeAt(0)];
  return nodeCounts;
};
