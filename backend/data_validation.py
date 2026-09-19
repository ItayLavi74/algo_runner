from algorithms_info import *


# checks if user input is valid, algorithm depended
def is_valid_data(data):
    response = {"is_valid": True,
                "message": ""}

    match data["algorithm"]:
        case "dijkstra":
            return checkInput(dijkstra_info, data)

    return {"is_valid": False,
            "message": ["unmatched 'algorithm'"]}


# check input to match algorithm assumptions, algo info from "backend/algorithms/algorithms_info.py"
def checkInput(algorithm_info: object, data: dict):
    response = {"is_valid": True,
                "messages": []}

    # start node:
    if algorithm_info.need_start_node:
        if data["startNode"] == "":
            response["is_valid"] = False
            response["messages"].append("Missing start node")

        elif data["startNode"] not in data["graph"]:
            response["is_valid"] = False
            response["messages"].append(
                "start node ins't a node in your graph")

    # edges sign:
    has_zero_edges = bool(data["edgesInfo"]["zero_edges"])
    has_negative_edges = bool(data["edgesInfo"]["negative_edges"])

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

    return response
