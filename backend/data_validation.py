
def isValidData(data):
    response = {"isValid": True,
                "message": ""}
    
    if needStartIndex(data["algoName"]):
        if data["startNode"] not in data["graph"]:
            response["isValid"] = False
            response["message"] = "start node isn't valid"
    
    return response


def needStartIndex(algoName):
    match algoName:
        case "dijkstra": return True
    return False