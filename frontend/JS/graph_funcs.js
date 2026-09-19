
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

    // checks if the graph is empty or has synax error
    if (!isPossibleGraph(userInput["graph"])) return

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

        if (!isLetter(a) || !isLetter(b) || !isNumber(weight)) {
            return [null, null]
        }

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

// Source - https://stackoverflow.com/a/32567789
// Posted by filip, modified by community. See post 'Timeline' for change history
// Retrieved 2026-09-18, License - CC BY-SA 3.0
function isLetter(c) {
    return c.toLowerCase() != c.toUpperCase();
}

function isNumber(x) {
    return typeof x === 'number';
}

function isPossibleGraph(graph) {
    if (graph == null) {
        window.alert(`Couldnt run algorithm: graph has SYNTAX ERROR`)
    }

    if (graph = "") {
        window.alert(`Couldnt run algorithm: EMPTY GRAPH`)
    }
}

