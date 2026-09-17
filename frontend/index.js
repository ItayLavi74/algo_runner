const output = document.getElementById("output");
const startNode = document.getElementById("startNode");
let needStartNode = false;
let algoName = "dijkstra";


async function run(){
    const textarea = document.querySelector('textarea');
    
    // create graph from txt input
    const graph = parseGraphFromText(textarea.value);
    
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
  const graph = {};
  const lines = text.trim().split('\n');

  for (const line of lines) {
    const [a, b, weight] = line.trim().split(/\s+/);
    const w = Number(weight);

    if (!graph[a]) graph[a] = {};
    if (!graph[b]) graph[b] = {};
    graph[a][b] = w;
    graph[b][a] = w;
  }

  return graph;
}

// modify the algorithm to user selection
function selectAlgo(str){
  algoName = str;
  console.log("algoName: ", algoName)
}
