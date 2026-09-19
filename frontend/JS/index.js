const output = document.getElementById("output");
const startNode = document.getElementById("startNode");
let needStartNode = false;
let algoName = "dijkstra";
let userInput = {};

// modify the algorithm to user selection
function selectAlgo(str) {
  algoName = str;
  console.log("algoName: ", algoName)
}

function getInput() {
  const textarea = document.querySelector('textarea');

  //build graph and detect its sign ('0<' if contain negative, '0' if non negative, '<0' if positive)
  const [graph, edgesInfo] = parseGraphInfoFromText(textarea.value);

  return {
    "algoName": algoName,
    "graph": graph,
    "edgesInfo": edgesInfo,
    "startNode": startNode.value
  }
}

async function run() {
  userInput = getInput();

  const response = await fetch("http://localhost:5000/api/receive", {
    method: "POST",
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(userInput)
  });
  const data = await response.text();

  // check if backend return error
  if (!response.ok) {
    window.alert(`Couldnt run algorithm: ${data}`)
  }
  else {
    output.textContent = data;
  }

}

// create graph (AL) from text input
function parseGraphInfoFromText(text) {
  let graphSign = 1; // '0<' if contain negative, '0' if non negative, '<0' if positive
  const graph = {};
  const lines = text.trim().split('\n');
  const edgesInfo = { "positive_edges": 0, "zero_edges": 0, "negative_edges": 0 };

  for (const line of lines) {
    const [a, b, weight] = line.trim().split(/\s+/);
    const w = Number(weight);

    if (!graph[a]) graph[a] = {};
    if (!graph[b]) graph[b] = {};
    graph[a][b] = w;
    graph[b][a] = w;

    // counting edges categorised by weight's sign
    if (w > 0)
      edgesInfo["positive_edges"] = + 1;
    else if (w == 0)
      edgesInfo["zero_edges"] = + 1;
    else
      edgesInfo["negative_edges"] = + 1;
  }

  return [graph, edgesInfo];
}

