import getGraphInfo from './graph_funcs.js';
import isInputSyntaxValid from './input_syntax_validation.js'


const output = document.getElementById("output");
const startNode = document.getElementById("startNode");
let needStartNode = false;
let algorithm = "";
let userInput = {};

document.getElementById('runButton').addEventListener('click', run)

// modify the algorithm to user selection
document.querySelectorAll('[name="algoSelect"]').forEach(elem => {
  elem.addEventListener('change', (event) => {
    algorithm = event.currentTarget.dataset.name;
    console.log("algorithm: ", algorithm);
  })
})


function getInput() {
  const textarea = document.querySelector('textarea');
  const graph = JSON.parse(textarea.value)

  return {
    "algorithm": algorithm,
    "graph":graph,
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
  const data = await response.json();

  console.log(response.status)

  // check if backend return error
  if (!response.ok) {
    window.alert(`Couldnt run algorithm: ${data}`)
  }
  else {
    output.textContent = JSON.stringify(data, null, 2);
  }
}
