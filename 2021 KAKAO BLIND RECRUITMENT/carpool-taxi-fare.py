import heapq


def dijkstra(graph, start, n):
    INF = float("inf")
    distances = [INF for _ in range(n + 1)]
    distances[start] = 0
    queue = []
    heapq.heappush(queue, (0, start))
    while queue:
        cur_cost, cur_node = heapq.heappop(queue)
        if distances[cur_node] < cur_cost:
            continue
        for node, cost in graph[cur_node]:
            new_cost = cur_cost + cost
            if new_cost < distances[node]:
                distances[node] = new_cost
                heapq.heappush(queue, (new_cost, node))
    return distances


def solution(n, s, a, b, fares):
    graph = [[] for _ in range(n + 1)]
    for fare in fares:
        node1, node2, cost = fare
        graph[node1].append((node2, cost))
        graph[node2].append((node1, cost))

    candidates = []
    for i in range(1, n + 1):
        distances1 = dijkstra(graph, s, n)
        carpool = distances1[i]
        distances2 = dijkstra(graph, i, n)
        single = distances2[a] + distances2[b]
        candidates.append(carpool + single)
    answer = min(candidates)
    return answer
