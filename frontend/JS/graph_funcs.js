// create graph (AL) from text input
export default function getGraphInfo(text) {
    const graph = {};
    const lines = text.trim().split('\n');
    const edgesInfo = { "positive_edges": 0, "zero_edges": 0, "negative_edges": 0 };

    for (const line of lines) {
        const [a, b, weight] = line.trim().split(/\s+/);
        const w = Number(weight);

        // checks typeof params
        if (!isLetter(a) || !isLetter(b) || !isNumber(w)) {
            return [null, null];
        }

        if (!graph[a]) graph[a] = {};
        if (!graph[b]) graph[b] = {};
        graph[a][b] = w;
        graph[b][a] = w;

        // counting edges categorised by weight's sign
        if (w > 0)
            edgesInfo["positive_edges"] += 1;
        else if (w == 0)
            edgesInfo["zero_edges"] += 1;
        else
            edgesInfo["negative_edges"] += 1;
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
    return typeof x === 'number' && !isNaN(x);
}


