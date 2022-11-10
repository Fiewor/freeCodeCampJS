let graph = new Map();
// store nodes, their neighbours and the cost of getting to that neighbour from the node
graph.set("start", new Map());
graph.get("start").set("a", 5);
graph.get("start").set("b", 2);

graph.set("a", new Map());
graph.get("a").set("c", 4);
graph.get("a").set("d", 2);

graph.set("b", new Map());
graph.get("b").set("a", 8);
graph.get("b").set("d", 7);

graph.set("c", new Map());
graph.get("c").set("finish", 3);
graph.get("c").set("d", 6);

graph.set("d", new Map());
graph.get("d").set("finish", 1);

// an hashtable for costs
let costs = {};
costs["a"] = 5;
costs["b"] = 2;
costs["c"] = Number.POSITIVE_INFINITY;
costs["d"] = Number.POSITIVE_INFINITY;
costs["finish"] = Number.POSITIVE_INFINITY;

costs;

// another hashTable for parents
let parents = {};
parents["a"] = "start";
parents["b"] = "start";
parents["c"] = "a";
parents["d"] = "b";
parents["finish"] = null;

let processed = [];

// find the cheapest node to get to from the start that hasn't been processed yet
const findLowestCodeNode = (node) => {
  let lowestCost = Number.POSITIVE_INFINITY;
  let lowestCostNode = null;
  for (const node in costs) {
    let cost = costs[node];
    if (cost < lowestCost) {
      lowestCost = cost;
      lowestCostNode = node;
    }
  }
  return lowestCostNode;
};

let node = findLowestCodeNode(costs);
if (!processed.includes(node)) {
  while (node) {
    let cost = costs[node];
    let neighbours = graph.get(node);
    for (const key of neighbours.keys()) {
      let newCost = cost + neighbours[key];
      if (newCost < costs[key]) {
        // if it's cheaper to get to this neighbor by going through this node
        costs[key] = newCost; // update the cost
        parents[key] = node; // update the parent of this node, basically choose to go through this route since it is cheaper
      }
    }
    processed.push(node);
    node = findLowestCodeNode(costs);
  }
}

console.log("costs", costs);
