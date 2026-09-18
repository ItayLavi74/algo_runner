const output = document.getElementById("output");
const startNode = document.getElementById("startNode");
let needStartNode = false;
let algoName = "dijkstra";

// modify the algorithm to user selection
function selectAlgo(str){
  algoName = str;
  console.log("algoName: ", algoName)
}

async function run(){
    const textarea = document.querySelector('textarea');
    
    // create graph from txt input
    const graph, graphSign = parseGraphFromText(textarea.value); //fix data los
    
    const response = await fetch("http://localhost:5000/api/receive", {
        method: "POST",
        headers: {
              'Content-Type': 'application/json'
        },
        body: JSON.stringify({"algoName": algoName,
                              "graph": graph,
                              "startNode": startNode.value
                              })
    });
    const data = await response.text();

    // check if backend return error
    if (!response.ok){
      window.alert(`Couldnt run algorithm: ${data}`)
    }
    else{
      output.textContent = data;
    }

}

// create graph (AL) from text input
function parseGraphFromText(text) {
  let graphSign = 1; // '0<' if contain negative, '0' if non negative, '<0' if positive
  const graph = {};
  const lines = text.trim().split('\n');

  for (const line of lines) {
    const [a, b, weight] = line.trim().split(/\s+/);
    const w = Number(weight);

    if (!graph[a]) graph[a] = {};
    if (!graph[b]) graph[b] = {};
    graph[a][b] = w;
    graph[b][a] = w;

    graphSign = Math.min(w, graphSign);
  }

  return graph, graphSign;
}

