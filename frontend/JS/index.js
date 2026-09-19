import getGraphInfo from './graph_funcs.js';
import isInputSyntaxValid from './input_syntax_validation.js'


const output = document.getElementById("output");
const startNode = document.getElementById("startNode");
let needStartNode = false;
let algoName = "";
let userInput = {};

document.getElementById('runButton').addEventListener('click', run)

document.querySelectorAll('[name="algoSelect"]').forEach(button => {
  button.addEventListener('change', (event) => {
    algoName = event.currentTarget.dataset.name;
    console.log("algoName: ", algoName);
  })
})

// // modify the algorithm to user selection
// export function selectAlgo(str) {
//   algoName = str;
//   console.log("algoName: ", algoName)
// }

function getInput() {
  const textarea = document.querySelector('textarea');

  const [graph, edgesInfo] = getGraphInfo(textarea.value);

  return {
    "algoName": algoName,
    "graph": graph,
    "edgesInfo": edgesInfo,
    "startNode": startNode.value
  }
}

async function run() {
  userInput = getInput();

  // checks if input has correct syntax
  if (!isInputSyntaxValid(userInput)) {
    window.alert(`Couldnt run algorithm: invalid input syntax`);
    return;
  }

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