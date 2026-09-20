from algorithms_info import *


# checks if user input is valid, algorithm depended
def is_valid_data(data):
    # response is currently a dead code
    response = {"is_valid": True,
                "messages": ""}

    # .get to handle empty data["algorithm"]
    match data.get("algorithm"):
        case "dijkstra":
            return checkInput(dijkstra_info, data)

    return {"is_valid": False,
            "messages": ["unmatched 'algorithm'"]}, 404


# check input to match algorithm assumptions, algo info from "backend/algorithms/algorithms_info.py"
def checkInput(algorithm_info: object, data: dict):
    response = {"is_valid": True,
                "messages": []}

    graph = data.get("graph")

    if (graph is None or len(graph) == 0):
        response["is_valid"] = False
        response["messages"].append("graph is empty or contain syntax error")
        return response, 400

    graph_info = checkGraph(graph)

    if (not graph_info["is_valid"]):
        response["is_valid"] = False
        response["messages"].append(
            "there is a neighbor that isn't a node in the graph")

    # start node:
    if algorithm_info.need_start_node:
        start_node = data.get("startNode")
        if start_node is None or start_node == "":
            response["is_valid"] = False
            response["messages"].append("Missing start node")

        elif start_node not in graph:
            response["is_valid"] = False
            response["messages"].append(
                "start node ins't a node in your graph")

    # edges sign:
    has_zero_edges = bool(graph_info["no_zero_edges"])
    has_negative_edges = bool(graph_info["no_negative_edges"])

    if algorithm_info.edge_sign_assump == EdgeSign.NON_ZERO and has_zero_edges:
        response["is_valid"] = False
        response["messages"].append("Graph CANNOT have edges with weight 0")

    if (algorithm_info.edge_sign_assump == EdgeSign.POSITIVE_ONLY
            and (has_negative_edges or has_zero_edges)):
        response["is_valid"] = False
        response["messages"].append("Graph can have ONLY POSITIVE edges")

    if (algorithm_info.edge_sign_assump == EdgeSign.NON_NEGATIVE
            and has_negative_edges):
        response["is_valid"] = False
        response["messages"].append(
            "Graph CANNOT have edges with NEGATIVE weight")

    return response, 200 if response["is_valid"] else 400


def checkGraph(graph: dict):
    flag = True  # indicates if there is a neighbor that isn't a node in the graph
    no_positive_edges = 0
    no_negative_edges = 0
    no_zero_edges = 0
    graph_nodes = graph.keys()

    for node in graph:
        for neighbor in graph[node]:
            if neighbor not in graph_nodes:
                flag = False

            w = graph[node][neighbor]
            if w > 0:
                no_positive_edges = no_positive_edges + 1
            elif w == 0:
                no_zero_edges = no_zero_edges + 1
            else:
                no_negative_edges = no_negative_edges + 1

    return {"is_valid": flag,
            "no_positive_edges": no_positive_edges,
            "no_zero_edges": no_zero_edges,
            "no_negative_edges": no_negative_edges}
