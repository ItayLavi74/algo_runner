from algorithm_documentation import AlgorithmStep


def dijkstra(graph, start):
    result = {}
    visited = {}

    for node in graph:
        result[node] = {'weight': float('inf'), 'previous': None}
    result[start]['weight'] = 0

    while True:
        current_node = None
        smallest_distance = float('inf')

        for node in result:
            if node not in visited and result[node]['weight'] < smallest_distance:
                smallest_distance = result[node]['weight']
                current_node = node

        if current_node is None:
            break

        visited[current_node] = True

        for neighbor, edge_weight in graph[current_node].items():
            new_distance = result[current_node]['weight'] + edge_weight

            if new_distance < result[neighbor]['weight']:
                result[neighbor]['weight'] = new_distance
                result[neighbor]['previous'] = current_node

    return None, result
