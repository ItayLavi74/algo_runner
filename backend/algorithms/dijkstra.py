from algorithm_documentation import AlgorithmStep
import copy


def dijkstra(data):
    graph = data["graph"]
    print("type of graph", type(graph))
    start = data["startNode"]
    result = {}
    visited = {}
    steps = []

    for node in graph:
        # None is treated like infinity
        result[node] = {'weight': None, 'previous': None}
        visited[node] = False
    result[start]['weight'] = 0

    steps.append(AlgorithmStep("init", {
        "graph": copy.deepcopy(result), "node": start, "scanned_node": None, "completed_nodes": visited.copy()}))

    while True:
        current_node = None
        smallest_distance = float('inf')

        # finding current node (smallest node that incomplete)
        for node in graph:
            steps.append(AlgorithmStep("scanning for uncompleted node with smallest distance", {
                "graph": copy.deepcopy(result), "node": current_node, "scanned_node": node, "completed_nodes": visited.copy()}))
            if (visited[node] or result[node]['weight'] is None):
                continue

            if (result[node]['weight'] < smallest_distance):
                smallest_distance = result[node]['weight']
                current_node = node

        steps.append(AlgorithmStep("found uncompleted node with smallest distance", {
                     "graph": copy.deepcopy(result), "node": current_node, "scanned_node": None, "completed_nodes": visited.copy()}))

        if current_node is None:
            steps.append(AlgorithmStep("all nodes completed", {
                "graph": copy.deepcopy(result), "node": current_node, "scanned_node": None, "completed_nodes": visited.copy()}))
            break

        visited[current_node] = True

        steps.append(AlgorithmStep("mark current node as completed", {
            "graph": copy.deepcopy(result), "node": current_node, "scanned_node": None, "completed_nodes": visited.copy()}))

        # checking if can get to neighbors from curr node with less distance
        for neighbor, edge_weight in graph[current_node].items():
            new_distance = result[current_node]['weight'] + edge_weight
            steps.append(AlgorithmStep("scanning neighbors", {
                "graph": copy.deepcopy(result), "node": current_node, "scanned_node": neighbor, "completed_nodes": visited.copy()}))

            if result[neighbor]['weight'] is None or new_distance < result[neighbor]['weight']:
                result[neighbor]['weight'] = new_distance
                result[neighbor]['previous'] = current_node
                steps.append(AlgorithmStep("updating distance", {
                    "graph": copy.deepcopy(result), "node": current_node, "scanned_node": neighbor, "completed_nodes": visited.copy()}))

    return steps, result
