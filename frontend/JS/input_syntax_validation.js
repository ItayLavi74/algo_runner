
// checks if user input has correct syntax
export default function isInputSyntaxValid(userInput) {
    if (!isPossibleGraph(userInput["graph"])) return false;

    return true;
}


function isPossibleGraph(graph) {
    if (graph == null) return false;

    if (graph == "") return false;

    return true
}