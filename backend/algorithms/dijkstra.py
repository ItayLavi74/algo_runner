# AI generated
def dijkstra(graph, start):
    distances = {}      # המרחק הקצר ביותר הידוע מ-start לכל צומת
    visited = {}         # צמתים שכבר "סגרנו"
    previous = {}        # לצורך שחזור המסלול בסוף

    # אתחול: כל המרחקים אינסוף חוץ מהצומת ההתחלתי
    for node in graph:
        distances[node] = float('inf')
        previous[node] = None
    distances[start] = 0

    while True:
        # מוצאים את הצומת הלא-מבוקר עם המרחק הקטן ביותר
        current_node = None
        smallest_distance = float('inf')

        for node in distances:
            if node not in visited and distances[node] < smallest_distance:
                smallest_distance = distances[node]
                current_node = node

        if current_node is None:
            break  # אין עוד צמתים נגישים

        visited[current_node] = True

        # בודקים את כל השכנים של הצומת הנוכחי
        for neighbor, weight in graph[current_node].items():
            new_distance = distances[current_node] + weight

            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                previous[neighbor] = current_node

    return distances, previous


def get_path(previous, target):
    path = []
    current = target

    while current is not None:
        path.insert(0, current)
        current = previous[current]

    return path